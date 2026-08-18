from itertools import product

def intervals(m):
    return [(a,b) for a in range(m+1) for b in range(a,m+1)]

def states_L(m, Ip, Iq, Ir):
    A,B=Ip; C,D=Iq; E,F=Ir
    return [(i,j,k,1+(j==k))
            for i in range(A,B+1) for j in range(C,D+1)
            for k in range(E,F+1) if j<=i and k<=i]

def states_V(m, Ip, Iq, Ir):
    A,B=Ip; C,D=Iq; E,F=Ir
    return [(i,j,k,1+(j==k))
            for i in range(A,B+1) for j in range(C,D+1)
            for k in range(E,F+1) if i<=j and i<=k]

def refl_interval(m, I):
    a,b=I
    return (m-b,m-a)

def marginal(states, coord, m):
    M=[0]*(m+1)
    for i,j,k,w in states:
        M[(i,j,k)[coord]] += w
    return M

def tails(M,h):
    return sum(M[:h]), M[h], sum(M[h+1:])

def orient_qr(states, direction):
    total=0
    for i,j,k,w in states:
        if direction == 'q<r':
            total += w if j<k else (1 if j==k else 0)
        else:
            total += w if k<j else (1 if j==k else 0)
    return total

checked=0
max_m=6
for m in range(max_m+1):
    Is=intervals(m)
    for Ip,Iq,Ir in product(Is, repeat=3):
        L=states_L(m,Ip,Iq,Ir)
        V=states_V(m,*(refl_interval(m,I) for I in (Ip,Iq,Ir)))
        assert sorted((m-i,m-j,m-k,w) for i,j,k,w in L)==sorted(V)
        NL=sum(w for i,j,k,w in L)
        assert NL==sum(w for i,j,k,w in V)
        for u in range(3):
            ML=marginal(L,u,m); MV=marginal(V,u,m)
            assert MV==list(reversed(ML))
            for h in range(m+1):
                assert tails(MV,m-h)==(tails(ML,h)[2],tails(ML,h)[1],tails(ML,h)[0])
        assert orient_qr(L,'q<r')+orient_qr(L,'r<q')==NL
        assert orient_qr(V,'q<r')==NL-orient_qr(L,'q<r')
        assert orient_qr(V,'r<q')==NL-orient_qr(L,'r<q')
        for t in range(1,m+1):
            s=m+1-t
            for u in range(3):
                SL=sum(w for row in L if row[u]<t for w in [row[3]])
                SV=sum(w for row in V if row[u]<s for w in [row[3]])
                assert SV==NL-SL
        checked += 1

m=2
Vraw=((0,1),(0,2),(0,2))
Lraw=tuple(refl_interval(m,I) for I in Vraw)
V=states_V(m,*Vraw); L=states_L(m,*Lraw)
Nv=sum(w for i,j,k,w in V)
Nl=sum(w for i,j,k,w in L)
Mv=[marginal(V,u,m) for u in range(3)]
Ml=[marginal(L,u,m) for u in range(3)]
assert (Nv,Nl)==(18,18)
assert Mv==[[12,6,0],[4,7,7],[4,7,7]]
assert Ml==[[0,6,12],[7,7,4],[7,7,4]]
assert sum(Mv[0][1:])==6 and sum(Mv[1][:2])==11
assert sum(Ml[0][:2])==6 and sum(Ml[1][1:])==11
facet_counts={'D<F':0,'D=F':0}
for m in range(7):
    for Ip,Iq,Ir in product(intervals(m), repeat=3):
        if Iq[1] <= Ir[1]:
            facet_counts['D=F' if Iq[1]==Ir[1] else 'D<F'] += 1
assert facet_counts=={'D<F':14388,'D=F':7056}
print('reflection_audit_max_m =',max_m)
print('reflection_state_fiber_checks =',checked)
print('all_state_weight_and_N_checks = PASS')
print('tail_exchange_checks = PASS')
print('orientation_complement_checks = PASS')
print('chain_endpoint_cuts_checked = all t=1..m for every m<=6')
print('cited_boundary_sample_V_intervals =',Vraw)
print('cited_boundary_sample_L_intervals =',Lraw)
print('cited_boundary_sample_N =',Nv)
print('cited_boundary_sample_V_marginals =',Mv)
print('cited_boundary_sample_L_marginals =',Ml)
print('cited_boundary_sample_V_H_L =',(6,11))
print('cited_boundary_sample_L_mapped_H_L =',(6,11))
print('canonical_V_facet_counts_m0_to_6 =',facet_counts)
print('status = ALL REFLECTION REGRESSION ASSERTIONS PASSED')
