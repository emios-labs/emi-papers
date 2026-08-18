from itertools import product, permutations
from collections import Counter


def intervals(m):
    return [(a,b) for a in range(m+1) for b in range(a,m+1)]


def refl_interval(m,I):
    a,b=I
    return (m-b,m-a)


def L_states(m, ip, iq, ir):
    A,B=ip; C,D=iq; E,F=ir
    return [(i,j,k,1+int(j==k))
            for i in range(A,B+1)
            for j in range(C,D+1)
            for k in range(E,F+1)
            if j<=i and k<=i]


def V_states(m, ip, iq, ir):
    A,B=ip; C,D=iq; E,F=ir
    return [(i,j,k,1+int(j==k)
            ) for i in range(A,B+1)
            for j in range(C,D+1)
            for k in range(E,F+1)
            if i<=j and i<=k]


def mass(states, coord, pred=lambda x: True):
    return sum(w for row in states if pred(row[coord]) for w in [row[3]])


def orient(states, which):
    ans=0
    for i,j,k,w in states:
        if which == 'q<r':
            ans += 1 if j<k or j==k else 0
        else:
            ans += 1 if k<j or j==k else 0
    return ans


def tails(states,coord,h):
    return (mass(states,coord,lambda x:x<h),
            mass(states,coord,lambda x:x==h),
            mass(states,coord,lambda x:x>h))


def relation_closure(nodes, edges):
    rel=set(edges)
    changed=True
    while changed:
        changed=False
        for a,b in tuple(rel):
            for c,d in tuple(rel):
                if b==c and (a,d) not in rel:
                    rel.add((a,d)); changed=True
    return rel


def make_base(m, intervals3, shape):
    nodes=[f'c{i}' for i in range(1,m+1)]+['p','q','r']
    e=set((f'c{i}',f'c{i+1}') for i in range(1,m))
    if shape=='L': e.update({('q','p'),('r','p')})
    else: e.update({('p','q'),('p','r')})
    for u,(a,b) in zip(['p','q','r'],intervals3):
        for t in range(1,m+1):
            if t<=a: e.add((f'c{t}',u))
            elif t>b: e.add((u,f'c{t}'))
    return nodes,relation_closure(nodes,e)


def legal_interval_from_rel(m, rel, u):
    legal=[]
    for x in range(m+1):
        ok=True
        for t in range(1,m+1):
            if (f'c{t}',u) in rel and not t<=x: ok=False
            if (u,f'c{t}') in rel and not x<t: ok=False
        if ok: legal.append(x)
    if not legal: return None
    assert legal==list(range(legal[0],legal[-1]+1)), (m,u,legal)
    return (legal[0],legal[-1])


def height(nodes,rel):
    indeg={u:0 for u in nodes}; out={u:[] for u in nodes}
    for a,b in rel:
        if a!=b: indeg[b]+=1; out[a].append(b)
    todo=[u for u in nodes if indeg[u]==0]; topo=[]
    while todo:
        u=todo.pop(); topo.append(u)
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0: todo.append(v)
    if len(topo)!=len(nodes): return None
    dp={u:1 for u in nodes}
    for u in topo:
        for v in out[u]: dp[v]=max(dp[v],dp[u]+1)
    return max(dp.values(),default=0)


def connected_incomp(nodes,rel):
    adj={u:set() for u in nodes}
    for ix,u in enumerate(nodes):
        for v in nodes[ix+1:]:
            if (u,v) not in rel and (v,u) not in rel:
                adj[u].add(v); adj[v].add(u)
    seen=set(); stack=[nodes[0]] if nodes else []
    while stack:
        u=stack.pop()
        if u in seen: continue
        seen.add(u); stack.extend(adj[u]-seen)
    return len(seen)==len(nodes)


def linexts(nodes,rel):
    out=[]
    for perm in permutations(nodes):
        pos={u:i for i,u in enumerate(perm)}
        if all(pos[a]<pos[b] for a,b in rel): out.append(perm)
    return out


def gap_of(word,m,u):
    pos=word.index(u)
    return sum(1 for z in word[:pos] if z.startswith('c'))


def state_count_from_words(words,m):
    d=Counter()
    for word in words:
        d[tuple(gap_of(word,m,u) for u in ['p','q','r'])]+=1
    return d


def dual_word(word,m):
    # P_L's c_t becomes P_V's d_{m+1-t}; defects retain labels.
    return tuple((f'c{m+1-int(z[1:])}' if z.startswith('c') else z) for z in reversed(word))


def actual_dual_interval_audit(max_m=5):
    checks=0; singleton=0
    for m in range(max_m+1):
        for raw in product(intervals(m),repeat=3):
            nodes,rel=make_base(m,raw,'L')
            if any((u,u) in rel for u in nodes): continue
            if ('q','r') in rel or ('r','q') in rel: continue
            if height(nodes,rel)!=m: continue
            ints=tuple(legal_interval_from_rel(m,rel,u) for u in ['p','q','r'])
            assert all(x is not None for x in ints), (m,raw,ints)
            if any(a==b for a,b in ints): singleton+=1
            Vints=tuple(refl_interval(m,I) for I in ints)
            vnodes,vrel=make_base(m,Vints,'V')
            assert not any((u,u) in vrel for u in vnodes)
            assert ('q','r') not in vrel and ('r','q') not in vrel
            assert height(vnodes,vrel)==m
            assert connected_incomp(nodes,rel)==connected_incomp(vnodes,vrel)
            wl=linexts(nodes,rel); wv=linexts(vnodes,vrel)
            assert len(wl)==len(wv)
            wvset=set(wv)
            assert all(dual_word(w,m) in wvset for w in wl)
            dl=state_count_from_words(wl,m)
            expected=Counter({(i,j,k):w for i,j,k,w in L_states(m,*ints)})
            assert dl==expected, (m,raw,ints,dl,expected)
            dv=state_count_from_words(wv,m)
            expectedv=Counter({(i,j,k):w for i,j,k,w in V_states(m,*Vints)})
            assert dv==expectedv, (m,raw,Vints,dv,expectedv)
            assert tuple(refl_interval(m,I) for I in ints)==Vints
            checks+=1
    return checks,singleton


def endpoint_domain_audit(max_m=5):
    checked=0; swapped=0
    for m in range(max_m+1):
        for raw in product(intervals(m),repeat=3):
            nodes,rel=make_base(m,raw,'L')
            if any((u,u) in rel for u in nodes): continue
            if ('q','r') in rel or ('r','q') in rel: continue
            if height(nodes,rel)!=m: continue
            ints=tuple(legal_interval_from_rel(m,rel,u) for u in ['p','q','r'])
            Vraw=tuple(refl_interval(m,I) for I in ints)
            if Vraw[1][1]>Vraw[2][1]:
                V=(Vraw[0],Vraw[2],Vraw[1]); swapped+=1
            else: V=Vraw
            (A,B),(C,D),(E,F)=V
            assert 0<=A<=B<=m and 0<=C<=D<=m and 0<=E<=F<=m
            assert A<=C and A<=E and B<=D and E<=D and D<=F, (m,ints,Vraw,V)
            assert all(b>a for a,b in V)
            checked+=1
    return checked,swapped


def interval_and_state_audit(max_m=8):
    state_checks=tail_checks=orientation_checks=cut_checks=diagonal_checks=threshold_eq=0
    empty_checks=0; facet=Counter(); max_n=0
    for m in range(max_m+1):
        for raw in product(intervals(m),repeat=3):
            L=L_states(m,*raw); Vints=tuple(refl_interval(m,I) for I in raw); V=V_states(m,*Vints)
            assert sorted((m-i,m-j,m-k,w) for i,j,k,w in L)==sorted(V)
            n=sum(w for *_,w in L); assert n==sum(w for *_,w in V); max_n=max(max_n,n)
            for u in range(3):
                for h in range(-2,m+3):
                    ll=tails(L,u,h); vv=tails(V,u,m-h)
                    assert vv==(ll[2],ll[1],ll[0]), (m,raw,u,h,ll,vv)
                    tail_checks+=1
                    threshold_eq += sum(int(3*z in (n,2*n)) for z in ll)
            sq=orient(L,'q<r'); sr=orient(L,'r<q')
            assert sq+sr==n and orient(V,'q<r')==sr==n-sq
            assert orient(V,'r<q')==sq==n-sr
            orientation_checks+=1
            d=sum(w for i,j,k,w in L if i==j==k)
            dv=sum(w for i,j,k,w in V if i==j==k)
            assert d==dv; diagonal_checks+=1
            for t in range(1,m+1):
                s=m+1-t
                for u in range(3):
                    lleft=mass(L,u,lambda x,t=t:x<t); lright=n-lleft
                    vcar=mass(V,u,lambda y,s=s:y>=s); vsame=mass(V,u,lambda y,s=s:y<s)
                    assert vcar==lleft and vsame==lright
                    cut_checks+=1
            for u,(a,b) in enumerate(raw):
                for t in range(1,m+1):
                    s=m+1-t
                    assert (a<t<=b)==(refl_interval(m,(a,b))[0]<s<=refl_interval(m,(a,b))[1])
            state_checks+=1
            D=Vints[1][1]; F=Vints[2][1]
            if D<=F: facet['D=F' if D==F else 'D<F']+=1
    for m in range(max_m+1):
        empty_checks+=1
        assert L_states(m,(1,0),(0,0),(0,0))==[]
        assert V_states(m,(1,0),(0,0),(0,0))==[]
    return state_checks,tail_checks,orientation_checks,cut_checks,diagonal_checks,threshold_eq,empty_checks,facet,max_n


def legal_interval_reflection_audit(max_m=8):
    checks=0
    for m in range(max_m+1):
        for a,b in intervals(m):
            legalL=[]
            for x in range(m+1):
                ok=True
                for t in range(1,m+1):
                    if t<=a and not t<=x: ok=False
                    if t>b and not x<t: ok=False
                if ok: legalL.append(x)
            assert legalL==list(range(a,b+1))
            relpred=[]
            for s in range(1,m+1):
                t=m+1-s
                # c_t<u in Lambda becomes u<d_s in V;
                # u<c_t in Lambda becomes d_s<u in V.
                if t<=a: relpred.append(('u<d',s))
                elif t>b: relpred.append(('d<u',s))
            legalV=[]
            for y in range(m+1):
                ok=True
                for typ,s in relpred:
                    if typ=='d<u' and not s<=y: ok=False
                    if typ=='u<d' and not y<s: ok=False
                if ok: legalV.append(y)
            assert legalV==list(range(m-b,m-a+1)), (m,a,b,relpred,legalV)
            checks+=1
    return checks


def heavy_relabel_audit(max_m=8):
    cases=swapped=mapped=0; examples=[]
    for m in range(max_m+1):
        for raw in product(intervals(m),repeat=3):
            L=L_states(m,*raw); n=sum(w for *_,w in L)
            if not n: continue
            heavy=[]
            for u in range(3):
                hs=[]
                for h in range(m+1):
                    lo,at,up=tails(L,u,h)
                    if 3*lo<n and 3*at>n and 3*up<n: hs.append(h)
                heavy.append(hs)
            for t in heavy[0]:
                for s in set(heavy[1]).intersection(heavy[2]):
                    if t>=s: continue
                    cases+=1
                    Vraw=tuple(refl_interval(m,I) for I in raw)
                    if Vraw[1][1]>Vraw[2][1]:
                        swapped+=1; qidx=2; ridx=1
                    else: qidx=1; ridx=2
                    V=(Vraw[0],Vraw[qidx],Vraw[ridx]); A=V[0][0]; D=V[1][1]
                    assert D==m-s and A==m-t and A<D
                    VV=V_states(m,*V); nv=sum(w for *_,w in VV); assert nv==n
                    H=mass(VV,0,lambda x:x>A); Lv=mass(VV,1,lambda x:x<D)
                    assert H==mass(L,0,lambda x:x<t)
                    orig_idx=qidx
                    assert Lv==mass(L,orig_idx,lambda x:x>s)
                    assert 3*H<n and 3*Lv<n
                    mapped+=1
                    if len(examples)<3: examples.append((m,raw,t,s,Vraw,V,H,Lv))
    return cases,swapped,mapped,examples


def complement_and_boundary_audit(max_n=50):
    checks=equality=0
    for n in range(max_n+1):
        for s in range(n+1):
            out=lambda x: 3*x<n or 3*x>2*n
            assert out(s)==out(n-s)
            equality += int(3*s in (n,2*n) or 3*(n-s) in (n,2*n))
            checks+=1
    return checks,equality


def main():
    print('LEGAL_INTERVAL_REFLECTION',legal_interval_reflection_audit(8))
    print('STATE_INTERVAL_REPLAY',interval_and_state_audit(8))
    print('ACTUAL_LINEAR_EXTENSION_DUAL_REPLAY',actual_dual_interval_audit(5))
    print('REALIZABILITY_ENDPOINT_DOMAIN_AUDIT',endpoint_domain_audit(5))
    print('HEAVY_CANONICAL_RELABEL_AUDIT',heavy_relabel_audit(8))
    print('CLOSED_THIRD_COMPLEMENT_AUDIT',complement_and_boundary_audit(50))
    print('STATUS ALL_INDEPENDENT_L2E_REFLECTION_ASSERTIONS_PASSED')

if __name__=='__main__': main()
