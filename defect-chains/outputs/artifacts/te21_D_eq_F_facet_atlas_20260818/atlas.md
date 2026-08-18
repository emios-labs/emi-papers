# TE(2=1) D=F Facet Chamber-and-Certificate Proof Object

**Disposition: COMPLETE.** This artifact closes the omitted normalized facet $f=F-D=0$ for every realizable guarded-V tied-siblings instance. It proves the stronger certificate $N\le 3L$, hence $N\le 3\max(H,L)$, on a 31-cell integer chamber envelope containing the exact structurally realizable facet.

Every substantive statement below carries one of the required honesty labels. The machine-readable full coefficient record is `outputs/data/te21_D_eq_F_facet_atlas_20260818.json`; the independent consumer is `outputs/code/replay_te21_D_eq_F_facet_atlas_20260818.py`; the generated human-readable certificate table is this file.

## 0. Scope and labels

**[PROVED-HERE]** The proof target is the exact facet $D=F$ in the normalized guarded-V model with defect order $p<q$, $p<r$, and $q\parallel r$. We do not rederive the already certified $f\ge1$ atlas.

**[COMPUTED]** The exact generator and its independent replay both completed all 31 cells. The replay log is quoted in §6 and deposited at `outputs/artifacts/te21_D_eq_F_facet_atlas_20260818/replay_report.txt`.

**[PROVED-HERE]** The final implication is obtained cell-by-cell from the displayed exact identities $3L-N=R_L$ with coefficientwise-nonnegative $R_L$.

## 1. Exact model, domain, and containment

### 1.1 Raw guarded-V realizability

**[ARGUED]** Use the attached authoritative guarded-V definitions. For closed integer gap intervals

$$I_p=[A,B],\qquad I_q=[C_0,D],\qquad I_r=[E,F],$$

the exact fiber set is
$$\Gamma=\{(i,j,k)\in I_p\times I_q\times I_r:i\le j,\ i\le k\},$$

and the exact tied-sibling fiber weight is $W(i,j,k)=1+\mathbf 1_{j=k}$. Thus $j=k$ contributes two extensions (one for each sibling orientation), including at $i=j=k$; it never contributes six.

**[ARGUED]** A raw tuple is `REALIZABLE_V` exactly when the endpoint relations and $p<q,p<r$ generate an acyclic transitive closure, $q\parallel r$, the displayed chain has height $m$, and the incomparability graph is connected, together with the exact endpoint/order guards from the authoritative executable predicate. After swapping $q,r$ we impose $D\le F$.

For clarity, the raw endpoint guard used for containment is the following exact one from the attached predicate:
$$0\le A\le B\le m,\quad 0\le C_0\le D\le m,\quad 0\le E\le F\le m,$$
$$A\le C_0,\quad A\le E,\quad B\le D,\quad E\le D,\quad D\le F,$$
together with the four structural checks just listed. The chamber proof below deliberately retains a larger envelope; any stronger exact endpoint clauses only remove cells/points and therefore cannot create a gap in the proof.

### 1.2 Translation and the omitted facet

**[PROVED-HERE]** Set $d=D$ and translate every gap by $-d$. Define
$$x=D-A,\quad y=D-B,\quad c=D-C_0,\quad e=D-E,\quad f=F-D.$$

Then
$$A=-x,\quad B=-y,\quad C_0=-c,\quad D=0,\quad E=-e,\quad F=f.$$

On $D=F$, $f=0$. Maximum-chain nonsingletonness gives $A<B$, $C_0<D$, $E<F$; the derived endpoint order gives $B\le D$. Consequently every realizable facet point lies in the exact certificate envelope
$$\mathcal E_0=\{(x,y,c,e)\in\mathbb Z^4:x>y\ge0,\ c\ge1,\ e\ge1\}.$$

The exact realizable facet is the more restrictive set
$$\mathcal R_0=\{(x,y,c,e)\in\mathcal E_0:\text{some translated raw tuple satisfies all exact REALIZABLE_V guards}\}.$$

**[PROVED-HERE]** Thus $\mathcal R_0\subseteq\mathcal E_0$. This is the required realizability containment: the atlas proves the target on $\mathcal E_0$, so it proves it for every actual $D=F$ instance. No sufficiency of the endpoint envelope is being silently claimed.

The envelope keeps the exact lower-bound/equality conventions: $y=0$, $c=1$, $e=1$, and $x=y+1$ are allowed. The exact structural checks may additionally force relations such as $A\le C_0$ or $A\le E$ in a particular raw presentation; those are not used to discard any of the 31 containment cells.

### 1.3 Exact event formulas and the target statistics

**[PROVED-HERE]** For any closed interval restrictions $P=[a,b]$, $Q=[q_0,q_1]$, $R=[r_0,r_1]$, with an empty restriction interpreted as zero, define $(t)_+=\max(t,0)$ and
$$\begin{aligned}
X_{j<k}(P,Q,R)&=\sum_{j=q_0}^{q_1}\big((j-a+1)_+-(j-b)_+\big)\big((r_1-j)_+-(r_0-1-j)_+\big),\\
X_{k<j}(P,Q,R)&=\sum_{k=r_0}^{r_1}\big((k-a+1)_+-(k-b)_+\big)\big((q_1-k)_+-(q_0-1-k)_+\big),\\
Y(P,Q,R)&=\sum_{h=\max(q_0,r_0)}^{\min(q_1,r_1)}\big((h-a+1)_+-(h-b)_+\big),\\
\mathcal V(P,Q,R)&=X_{j<k}(P,Q,R)+X_{k<j}(P,Q,R)+2Y(P,Q,R).
\end{aligned}$$

The first product counts $i\le j$ and $k>j$; the second counts $i\le k$ and $j>k$; the last line is the tied diagonal with weight two. This is the attached exact ledger written in a form used by the replay.

**[PROVED-HERE]** In every cell,
$$N=\mathcal V(I_p,I_q,I_r),\qquad H=\mathcal V([A+1,B],I_q,I_r),\qquad L=\mathcal V(I_p,[C_0,D-1],I_r).$$
Thus $H=U_p(A)$ and $L=L_q(D)$ with the strict tails literal: $i=A$ is excluded from $H$, while $j=D$ is excluded from $L$.

## 2. Exhaustive chamber atlas and boundary conventions

**[PROVED-HERE]** A bar `|` means a strict increase of integer levels; letters in one block are equal. The 31 patterns below are the ordered partitions of $\{x,y,c,e\}$ with $x>y$, listed in increasing level order. Each strict level gap is exactly $1+z_i$ with $z_i\ge0$. The lowest level is `offset + shift + u`, with $u\ge0$; `shift=1` precisely when $e$ is on the lowest level and $c$ is not, enforcing the facet condition $e\ge1$.

The variables in every row are independent nonnegative integers. Equality of two labels is represented only by placing them in one block; $z_i=0$ means adjacent distinct integer levels, not equality. At $f=0$, $D=F=0$ is an equality boundary and there is no $v$ variable. These conventions cover all weak/equality faces, including $e=1$ in the shifted rows.

**[PROVED-HERE]** Conversely, given any $(x,y,c,e)\in\mathcal E_0$, sort its four values, group equal values, and recover $u$ and each $z_i$ from the lowest level and consecutive gaps. This yields exactly one row and nonnegative variables. Therefore the rows cover $\mathcal E_0$ disjointly.

### Cell 0: `y|xce`

**[PROVED-HERE]** Blocks: `y|xce`; variables: u, z0; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $x=u + z0 + 1$, $c=u + z0 + 1$, $e=u + z0 + 1$.

Endpoints: $A=-u - z0 - 1$, $B=-u$, $C0=-u - z0 - 1$, $D=0$, $E=-u - z0 - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=8 + 26/3\,z0 + 3\,z0^2 + 1/3\,z0^3 + 8\,u + 6\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

$$H=2 + 11/3\,z0 + 2\,z0^2 + 1/3\,z0^3 + 3\,u + 4\,u\,z0 + u\,z0^2 + u^2 + u^2\,z0$$

$$L=3 + 31/6\,z0 + 5/2\,z0^2 + 1/3\,z0^3 + 6\,u + 5\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=1 + 41/6\,z0 + 9/2\,z0^2 + 2/3\,z0^3 + 10\,u + 9\,u\,z0 + 2\,u\,z0^2 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 1: `yc|xe`

**[PROVED-HERE]** Blocks: `yc|xe`; variables: u, z0; `offset=1`, `shift=0`, all nonnegative integers.

Levels: $y=u + 1$, $c=u + 1$, $x=u + z0 + 2$, $e=u + z0 + 2$.

Endpoints: $A=-u - z0 - 2$, $B=-u - 1$, $C0=-u - 1$, $D=0$, $E=-u - z0 - 2$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=14 + 9\,z0 + z0^2 + 11\,u + 13/2\,u\,z0 + 1/2\,u\,z0^2 + 2\,u^2 + u^2\,z0$$

$$H=6 + 7\,z0 + z0^2 + 5\,u + 11/2\,u\,z0 + 1/2\,u\,z0^2 + u^2 + u^2\,z0$$

$$L=7 + 9/2\,z0 + 1/2\,z0^2 + 9\,u + 11/2\,u\,z0 + 1/2\,u\,z0^2 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=7 + 9/2\,z0 + 1/2\,z0^2 + 16\,u + 10\,u\,z0 + u\,z0^2 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 2: `yce|x`

**[PROVED-HERE]** Blocks: `yce|x`; variables: u, z0; `offset=1`, `shift=0`, all nonnegative integers.

Levels: $y=u + 1$, $c=u + 1$, $e=u + 1$, $x=u + z0 + 2$.

Endpoints: $A=-u - z0 - 2$, $B=-u - 1$, $C0=-u - 1$, $D=0$, $E=-u - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=12 + 6\,z0 + 10\,u + 5\,u\,z0 + 2\,u^2 + u^2\,z0$$

$$H=6 + 6\,z0 + 5\,u + 5\,u\,z0 + u^2 + u^2\,z0$$

$$L=6 + 3\,z0 + 8\,u + 4\,u\,z0 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=6 + 3\,z0 + 14\,u + 7\,u\,z0 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 3: `ye|xc`

**[PROVED-HERE]** Blocks: `ye|xc`; variables: u, z0; `offset=0`, `shift=1`, all nonnegative integers.

Levels: $y=u + 1$, $e=u + 1$, $x=u + z0 + 2$, $c=u + z0 + 2$.

Endpoints: $A=-u - z0 - 2$, $B=-u - 1$, $C0=-u - z0 - 2$, $D=0$, $E=-u - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=14 + 9\,z0 + z0^2 + 11\,u + 13/2\,u\,z0 + 1/2\,u\,z0^2 + 2\,u^2 + u^2\,z0$$

$$H=6 + 7\,z0 + z0^2 + 5\,u + 11/2\,u\,z0 + 1/2\,u\,z0^2 + u^2 + u^2\,z0$$

$$L=8 + 6\,z0 + z0^2 + 9\,u + 11/2\,u\,z0 + 1/2\,u\,z0^2 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=10 + 9\,z0 + 2\,z0^2 + 16\,u + 10\,u\,z0 + u\,z0^2 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 4: `c|y|xe`

**[PROVED-HERE]** Blocks: `c|y|xe`; variables: u, z0, z1; `offset=1`, `shift=0`, all nonnegative integers.

Levels: $c=u + 1$, $y=u + z0 + 2$, $x=u + z0 + z1 + 3$, $e=u + z0 + z1 + 3$.

Endpoints: $A=-u - z0 - z1 - 3$, $B=-u - z0 - 2$, $C0=-u - 1$, $D=0$, $E=-u - z0 - z1 - 3$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=18 + 11\,z1 + z1^2 + 4\,z0 + 2\,z0\,z1 + 13\,u + 15/2\,u\,z1 + 1/2\,u\,z1^2 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

$$H=8 + 9\,z1 + z1^2 + 2\,z0 + 2\,z0\,z1 + 6\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + u\,z0 + u\,z0\,z1 + u^2 + u^2\,z1$$

$$L=9 + 11/2\,z1 + 1/2\,z1^2 + 2\,z0 + z0\,z1 + 11\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=9 + 11/2\,z1 + 1/2\,z1^2 + 2\,z0 + z0\,z1 + 20\,u + 12\,u\,z1 + u\,z1^2 + 4\,u\,z0 + 2\,u\,z0\,z1 + 4\,u^2 + 2\,u^2\,z1$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 5: `c|ye|x`

**[PROVED-HERE]** Blocks: `c|ye|x`; variables: u, z0, z1; `offset=1`, `shift=0`, all nonnegative integers.

Levels: $c=u + 1$, $y=u + z0 + 2$, $e=u + z0 + 2$, $x=u + z0 + z1 + 3$.

Endpoints: $A=-u - z0 - z1 - 3$, $B=-u - z0 - 2$, $C0=-u - 1$, $D=0$, $E=-u - z0 - 2$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=16 + 8\,z1 + 4\,z0 + 2\,z0\,z1 + 12\,u + 6\,u\,z1 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

$$H=8 + 8\,z1 + 2\,z0 + 2\,z0\,z1 + 6\,u + 6\,u\,z1 + u\,z0 + u\,z0\,z1 + u^2 + u^2\,z1$$

$$L=8 + 4\,z1 + 2\,z0 + z0\,z1 + 10\,u + 5\,u\,z1 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=8 + 4\,z1 + 2\,z0 + z0\,z1 + 18\,u + 9\,u\,z1 + 4\,u\,z0 + 2\,u\,z0\,z1 + 4\,u^2 + 2\,u^2\,z1$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 6: `ce|y|x`

**[PROVED-HERE]** Blocks: `ce|y|x`; variables: u, z0, z1; `offset=1`, `shift=0`, all nonnegative integers.

Levels: $c=u + 1$, $e=u + 1$, $y=u + z0 + 2$, $x=u + z0 + z1 + 3$.

Endpoints: $A=-u - z0 - z1 - 3$, $B=-u - z0 - 2$, $C0=-u - 1$, $D=0$, $E=-u - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=12 + 6\,z1 + 10\,u + 5\,u\,z1 + 2\,u^2 + u^2\,z1$$

$$H=6 + 6\,z1 + 5\,u + 5\,u\,z1 + u^2 + u^2\,z1$$

$$L=6 + 3\,z1 + 8\,u + 4\,u\,z1 + 2\,u^2 + u^2\,z1$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=6 + 3\,z1 + 14\,u + 7\,u\,z1 + 4\,u^2 + 2\,u^2\,z1$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 7: `e|y|xc`

**[PROVED-HERE]** Blocks: `e|y|xc`; variables: u, z0, z1; `offset=0`, `shift=1`, all nonnegative integers.

Levels: $e=u + 1$, $y=u + z0 + 2$, $x=u + z0 + z1 + 3$, $c=u + z0 + z1 + 3$.

Endpoints: $A=-u - z0 - z1 - 3$, $B=-u - z0 - 2$, $C0=-u - z0 - z1 - 3$, $D=0$, $E=-u - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=18 + 11\,z1 + z1^2 + 4\,z0 + 2\,z0\,z1 + 13\,u + 15/2\,u\,z1 + 1/2\,u\,z1^2 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

$$H=8 + 9\,z1 + z1^2 + 2\,z0 + 2\,z0\,z1 + 6\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + u\,z0 + u\,z0\,z1 + u^2 + u^2\,z1$$

$$L=12 + 8\,z1 + z1^2 + 4\,z0 + 2\,z0\,z1 + 11\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=18 + 13\,z1 + 2\,z1^2 + 8\,z0 + 4\,z0\,z1 + 20\,u + 12\,u\,z1 + u\,z1^2 + 4\,u\,z0 + 2\,u\,z0\,z1 + 4\,u^2 + 2\,u^2\,z1$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 8: `e|yc|x`

**[PROVED-HERE]** Blocks: `e|yc|x`; variables: u, z0, z1; `offset=0`, `shift=1`, all nonnegative integers.

Levels: $e=u + 1$, $y=u + z0 + 2$, $c=u + z0 + 2$, $x=u + z0 + z1 + 3$.

Endpoints: $A=-u - z0 - z1 - 3$, $B=-u - z0 - 2$, $C0=-u - z0 - 2$, $D=0$, $E=-u - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=16 + 8\,z1 + 4\,z0 + 2\,z0\,z1 + 12\,u + 6\,u\,z1 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

$$H=8 + 8\,z1 + 2\,z0 + 2\,z0\,z1 + 6\,u + 6\,u\,z1 + u\,z0 + u\,z0\,z1 + u^2 + u^2\,z1$$

$$L=10 + 5\,z1 + 4\,z0 + 2\,z0\,z1 + 10\,u + 5\,u\,z1 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=14 + 7\,z1 + 8\,z0 + 4\,z0\,z1 + 18\,u + 9\,u\,z1 + 4\,u\,z0 + 2\,u\,z0\,z1 + 4\,u^2 + 2\,u^2\,z1$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 9: `y|c|xe`

**[PROVED-HERE]** Blocks: `y|c|xe`; variables: u, z0, z1; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $c=u + z0 + 1$, $x=u + z0 + z1 + 2$, $e=u + z0 + z1 + 2$.

Endpoints: $A=-u - z0 - z1 - 2$, $B=-u$, $C0=-u - z0 - 1$, $D=0$, $E=-u - z0 - z1 - 2$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=16 + 9\,z1 + z1^2 + 44/3\,z0 + 13/2\,z0\,z1 + 1/2\,z0\,z1^2 + 4\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 14\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + 8\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

$$H=8 + 7\,z1 + z1^2 + 26/3\,z0 + 11/2\,z0\,z1 + 1/2\,z0\,z1^2 + 3\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 8\,u + 11/2\,u\,z1 + 1/2\,u\,z1^2 + 6\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 2\,u^2 + u^2\,z1 + u^2\,z0$$

$$L=7 + 9/2\,z1 + 1/2\,z1^2 + 61/6\,z0 + 11/2\,z0\,z1 + 1/2\,z0\,z1^2 + 7/2\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 11\,u + 11/2\,u\,z1 + 1/2\,u\,z1^2 + 7\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=5 + 9/2\,z1 + 1/2\,z1^2 + 95/6\,z0 + 10\,z0\,z1 + z0\,z1^2 + 13/2\,z0^2 + 2\,z0^2\,z1 + 2/3\,z0^3 + 19\,u + 10\,u\,z1 + u\,z1^2 + 13\,u\,z0 + 4\,u\,z0\,z1 + 2\,u\,z0^2 + 6\,u^2 + 2\,u^2\,z1 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 10: `y|ce|x`

**[PROVED-HERE]** Blocks: `y|ce|x`; variables: u, z0, z1; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $c=u + z0 + 1$, $e=u + z0 + 1$, $x=u + z0 + z1 + 2$.

Endpoints: $A=-u - z0 - z1 - 2$, $B=-u$, $C0=-u - z0 - 1$, $D=0$, $E=-u - z0 - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=14 + 6\,z1 + 41/3\,z0 + 5\,z0\,z1 + 4\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 13\,u + 5\,u\,z1 + 8\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

$$H=8 + 6\,z1 + 26/3\,z0 + 5\,z0\,z1 + 3\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 8\,u + 5\,u\,z1 + 6\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 2\,u^2 + u^2\,z1 + u^2\,z0$$

$$L=6 + 3\,z1 + 55/6\,z0 + 4\,z0\,z1 + 7/2\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 10\,u + 4\,u\,z1 + 7\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=4 + 3\,z1 + 83/6\,z0 + 7\,z0\,z1 + 13/2\,z0^2 + 2\,z0^2\,z1 + 2/3\,z0^3 + 17\,u + 7\,u\,z1 + 13\,u\,z0 + 4\,u\,z0\,z1 + 2\,u\,z0^2 + 6\,u^2 + 2\,u^2\,z1 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 11: `y|e|xc`

**[PROVED-HERE]** Blocks: `y|e|xc`; variables: u, z0, z1; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $e=u + z0 + 1$, $x=u + z0 + z1 + 2$, $c=u + z0 + z1 + 2$.

Endpoints: $A=-u - z0 - z1 - 2$, $B=-u$, $C0=-u - z0 - z1 - 2$, $D=0$, $E=-u - z0 - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=16 + 9\,z1 + z1^2 + 44/3\,z0 + 13/2\,z0\,z1 + 1/2\,z0\,z1^2 + 4\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 14\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + 8\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

$$H=8 + 7\,z1 + z1^2 + 26/3\,z0 + 11/2\,z0\,z1 + 1/2\,z0\,z1^2 + 3\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 8\,u + 11/2\,u\,z1 + 1/2\,u\,z1^2 + 6\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 2\,u^2 + u^2\,z1 + u^2\,z0$$

$$L=8 + 6\,z1 + z1^2 + 61/6\,z0 + 11/2\,z0\,z1 + 1/2\,z0\,z1^2 + 7/2\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 11\,u + 11/2\,u\,z1 + 1/2\,u\,z1^2 + 7\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=8 + 9\,z1 + 2\,z1^2 + 95/6\,z0 + 10\,z0\,z1 + z0\,z1^2 + 13/2\,z0^2 + 2\,z0^2\,z1 + 2/3\,z0^3 + 19\,u + 10\,u\,z1 + u\,z1^2 + 13\,u\,z0 + 4\,u\,z0\,z1 + 2\,u\,z0^2 + 6\,u^2 + 2\,u^2\,z1 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 12: `y|x|ce`

**[PROVED-HERE]** Blocks: `y|x|ce`; variables: u, z0, z1; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $x=u + z0 + 1$, $c=u + z0 + z1 + 2$, $e=u + z0 + z1 + 2$.

Endpoints: $A=-u - z0 - 1$, $B=-u$, $C0=-u - z0 - z1 - 2$, $D=0$, $E=-u - z0 - z1 - 2$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=8 + 26/3\,z0 + 3\,z0^2 + 1/3\,z0^3 + 8\,u + 6\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

$$H=2 + 11/3\,z0 + 2\,z0^2 + 1/3\,z0^3 + 3\,u + 4\,u\,z0 + u\,z0^2 + u^2 + u^2\,z0$$

$$L=3 + 31/6\,z0 + 5/2\,z0^2 + 1/3\,z0^3 + 6\,u + 5\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=1 + 41/6\,z0 + 9/2\,z0^2 + 2/3\,z0^3 + 10\,u + 9\,u\,z0 + 2\,u\,z0^2 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 13: `y|xc|e`

**[PROVED-HERE]** Blocks: `y|xc|e`; variables: u, z0, z1; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $x=u + z0 + 1$, $c=u + z0 + 1$, $e=u + z0 + z1 + 2$.

Endpoints: $A=-u - z0 - 1$, $B=-u$, $C0=-u - z0 - 1$, $D=0$, $E=-u - z0 - z1 - 2$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=8 + 26/3\,z0 + 3\,z0^2 + 1/3\,z0^3 + 8\,u + 6\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

$$H=2 + 11/3\,z0 + 2\,z0^2 + 1/3\,z0^3 + 3\,u + 4\,u\,z0 + u\,z0^2 + u^2 + u^2\,z0$$

$$L=3 + 31/6\,z0 + 5/2\,z0^2 + 1/3\,z0^3 + 6\,u + 5\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=1 + 41/6\,z0 + 9/2\,z0^2 + 2/3\,z0^3 + 10\,u + 9\,u\,z0 + 2\,u\,z0^2 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 14: `y|xe|c`

**[PROVED-HERE]** Blocks: `y|xe|c`; variables: u, z0, z1; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $x=u + z0 + 1$, $e=u + z0 + 1$, $c=u + z0 + z1 + 2$.

Endpoints: $A=-u - z0 - 1$, $B=-u$, $C0=-u - z0 - z1 - 2$, $D=0$, $E=-u - z0 - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=8 + 26/3\,z0 + 3\,z0^2 + 1/3\,z0^3 + 8\,u + 6\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

$$H=2 + 11/3\,z0 + 2\,z0^2 + 1/3\,z0^3 + 3\,u + 4\,u\,z0 + u\,z0^2 + u^2 + u^2\,z0$$

$$L=3 + 31/6\,z0 + 5/2\,z0^2 + 1/3\,z0^3 + 6\,u + 5\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=1 + 41/6\,z0 + 9/2\,z0^2 + 2/3\,z0^3 + 10\,u + 9\,u\,z0 + 2\,u\,z0^2 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 15: `yc|e|x`

**[PROVED-HERE]** Blocks: `yc|e|x`; variables: u, z0, z1; `offset=1`, `shift=0`, all nonnegative integers.

Levels: $y=u + 1$, $c=u + 1$, $e=u + z0 + 2$, $x=u + z0 + z1 + 3$.

Endpoints: $A=-u - z0 - z1 - 3$, $B=-u - 1$, $C0=-u - 1$, $D=0$, $E=-u - z0 - 2$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=22 + 8\,z1 + 11\,z0 + 2\,z0\,z1 + z0^2 + 17\,u + 6\,u\,z1 + 15/2\,u\,z0 + u\,z0\,z1 + 1/2\,u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

$$H=14 + 8\,z1 + 9\,z0 + 2\,z0\,z1 + z0^2 + 11\,u + 6\,u\,z1 + 13/2\,u\,z0 + u\,z0\,z1 + 1/2\,u\,z0^2 + 2\,u^2 + u^2\,z1 + u^2\,z0$$

$$L=11 + 4\,z1 + 11/2\,z0 + z0\,z1 + 1/2\,z0^2 + 14\,u + 5\,u\,z1 + 13/2\,u\,z0 + u\,z0\,z1 + 1/2\,u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=11 + 4\,z1 + 11/2\,z0 + z0\,z1 + 1/2\,z0^2 + 25\,u + 9\,u\,z1 + 12\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 6\,u^2 + 2\,u^2\,z1 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 16: `yc|x|e`

**[PROVED-HERE]** Blocks: `yc|x|e`; variables: u, z0, z1; `offset=1`, `shift=0`, all nonnegative integers.

Levels: $y=u + 1$, $c=u + 1$, $x=u + z0 + 2$, $e=u + z0 + z1 + 3$.

Endpoints: $A=-u - z0 - 2$, $B=-u - 1$, $C0=-u - 1$, $D=0$, $E=-u - z0 - z1 - 3$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=14 + 9\,z0 + z0^2 + 11\,u + 13/2\,u\,z0 + 1/2\,u\,z0^2 + 2\,u^2 + u^2\,z0$$

$$H=6 + 7\,z0 + z0^2 + 5\,u + 11/2\,u\,z0 + 1/2\,u\,z0^2 + u^2 + u^2\,z0$$

$$L=7 + 9/2\,z0 + 1/2\,z0^2 + 9\,u + 11/2\,u\,z0 + 1/2\,u\,z0^2 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=7 + 9/2\,z0 + 1/2\,z0^2 + 16\,u + 10\,u\,z0 + u\,z0^2 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 17: `ye|c|x`

**[PROVED-HERE]** Blocks: `ye|c|x`; variables: u, z0, z1; `offset=0`, `shift=1`, all nonnegative integers.

Levels: $y=u + 1$, $e=u + 1$, $c=u + z0 + 2$, $x=u + z0 + z1 + 3$.

Endpoints: $A=-u - z0 - z1 - 3$, $B=-u - 1$, $C0=-u - z0 - 2$, $D=0$, $E=-u - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=22 + 8\,z1 + 11\,z0 + 2\,z0\,z1 + z0^2 + 17\,u + 6\,u\,z1 + 15/2\,u\,z0 + u\,z0\,z1 + 1/2\,u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

$$H=14 + 8\,z1 + 9\,z0 + 2\,z0\,z1 + z0^2 + 11\,u + 6\,u\,z1 + 13/2\,u\,z0 + u\,z0\,z1 + 1/2\,u\,z0^2 + 2\,u^2 + u^2\,z1 + u^2\,z0$$

$$L=13 + 5\,z1 + 8\,z0 + 2\,z0\,z1 + z0^2 + 14\,u + 5\,u\,z1 + 13/2\,u\,z0 + u\,z0\,z1 + 1/2\,u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=17 + 7\,z1 + 13\,z0 + 4\,z0\,z1 + 2\,z0^2 + 25\,u + 9\,u\,z1 + 12\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 6\,u^2 + 2\,u^2\,z1 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 18: `ye|x|c`

**[PROVED-HERE]** Blocks: `ye|x|c`; variables: u, z0, z1; `offset=0`, `shift=1`, all nonnegative integers.

Levels: $y=u + 1$, $e=u + 1$, $x=u + z0 + 2$, $c=u + z0 + z1 + 3$.

Endpoints: $A=-u - z0 - 2$, $B=-u - 1$, $C0=-u - z0 - z1 - 3$, $D=0$, $E=-u - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=14 + 9\,z0 + z0^2 + 11\,u + 13/2\,u\,z0 + 1/2\,u\,z0^2 + 2\,u^2 + u^2\,z0$$

$$H=6 + 7\,z0 + z0^2 + 5\,u + 11/2\,u\,z0 + 1/2\,u\,z0^2 + u^2 + u^2\,z0$$

$$L=8 + 6\,z0 + z0^2 + 9\,u + 11/2\,u\,z0 + 1/2\,u\,z0^2 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=10 + 9\,z0 + 2\,z0^2 + 16\,u + 10\,u\,z0 + u\,z0^2 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 19: `c|e|y|x`

**[PROVED-HERE]** Blocks: `c|e|y|x`; variables: u, z0, z1, z2; `offset=1`, `shift=0`, all nonnegative integers.

Levels: $c=u + 1$, $e=u + z0 + 2$, $y=u + z0 + z1 + 3$, $x=u + z0 + z1 + z2 + 4$.

Endpoints: $A=-u - z0 - z1 - z2 - 4$, $B=-u - z0 - z1 - 3$, $C0=-u - 1$, $D=0$, $E=-u - z0 - 2$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=16 + 8\,z2 + 4\,z0 + 2\,z0\,z2 + 12\,u + 6\,u\,z2 + 2\,u\,z0 + u\,z0\,z2 + 2\,u^2 + u^2\,z2$$

$$H=8 + 8\,z2 + 2\,z0 + 2\,z0\,z2 + 6\,u + 6\,u\,z2 + u\,z0 + u\,z0\,z2 + u^2 + u^2\,z2$$

$$L=8 + 4\,z2 + 2\,z0 + z0\,z2 + 10\,u + 5\,u\,z2 + 2\,u\,z0 + u\,z0\,z2 + 2\,u^2 + u^2\,z2$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=8 + 4\,z2 + 2\,z0 + z0\,z2 + 18\,u + 9\,u\,z2 + 4\,u\,z0 + 2\,u\,z0\,z2 + 4\,u^2 + 2\,u^2\,z2$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 20: `c|y|e|x`

**[PROVED-HERE]** Blocks: `c|y|e|x`; variables: u, z0, z1, z2; `offset=1`, `shift=0`, all nonnegative integers.

Levels: $c=u + 1$, $y=u + z0 + 2$, $e=u + z0 + z1 + 3$, $x=u + z0 + z1 + z2 + 4$.

Endpoints: $A=-u - z0 - z1 - z2 - 4$, $B=-u - z0 - 2$, $C0=-u - 1$, $D=0$, $E=-u - z0 - z1 - 3$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=28 + 10\,z2 + 13\,z1 + 2\,z1\,z2 + z1^2 + 6\,z0 + 2\,z0\,z2 + 2\,z0\,z1 + 20\,u + 7\,u\,z2 + 17/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 3\,u\,z0 + u\,z0\,z2 + u\,z0\,z1 + 3\,u^2 + u^2\,z2 + u^2\,z1$$

$$H=18 + 10\,z2 + 11\,z1 + 2\,z1\,z2 + z1^2 + 4\,z0 + 2\,z0\,z2 + 2\,z0\,z1 + 13\,u + 7\,u\,z2 + 15/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 2\,u\,z0 + u\,z0\,z2 + u\,z0\,z1 + 2\,u^2 + u^2\,z2 + u^2\,z1$$

$$L=14 + 5\,z2 + 13/2\,z1 + z1\,z2 + 1/2\,z1^2 + 3\,z0 + z0\,z2 + z0\,z1 + 17\,u + 6\,u\,z2 + 15/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 3\,u\,z0 + u\,z0\,z2 + u\,z0\,z1 + 3\,u^2 + u^2\,z2 + u^2\,z1$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=14 + 5\,z2 + 13/2\,z1 + z1\,z2 + 1/2\,z1^2 + 3\,z0 + z0\,z2 + z0\,z1 + 31\,u + 11\,u\,z2 + 14\,u\,z1 + 2\,u\,z1\,z2 + u\,z1^2 + 6\,u\,z0 + 2\,u\,z0\,z2 + 2\,u\,z0\,z1 + 6\,u^2 + 2\,u^2\,z2 + 2\,u^2\,z1$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 21: `c|y|x|e`

**[PROVED-HERE]** Blocks: `c|y|x|e`; variables: u, z0, z1, z2; `offset=1`, `shift=0`, all nonnegative integers.

Levels: $c=u + 1$, $y=u + z0 + 2$, $x=u + z0 + z1 + 3$, $e=u + z0 + z1 + z2 + 4$.

Endpoints: $A=-u - z0 - z1 - 3$, $B=-u - z0 - 2$, $C0=-u - 1$, $D=0$, $E=-u - z0 - z1 - z2 - 4$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=18 + 11\,z1 + z1^2 + 4\,z0 + 2\,z0\,z1 + 13\,u + 15/2\,u\,z1 + 1/2\,u\,z1^2 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

$$H=8 + 9\,z1 + z1^2 + 2\,z0 + 2\,z0\,z1 + 6\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + u\,z0 + u\,z0\,z1 + u^2 + u^2\,z1$$

$$L=9 + 11/2\,z1 + 1/2\,z1^2 + 2\,z0 + z0\,z1 + 11\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=9 + 11/2\,z1 + 1/2\,z1^2 + 2\,z0 + z0\,z1 + 20\,u + 12\,u\,z1 + u\,z1^2 + 4\,u\,z0 + 2\,u\,z0\,z1 + 4\,u^2 + 2\,u^2\,z1$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 22: `e|c|y|x`

**[PROVED-HERE]** Blocks: `e|c|y|x`; variables: u, z0, z1, z2; `offset=0`, `shift=1`, all nonnegative integers.

Levels: $e=u + 1$, $c=u + z0 + 2$, $y=u + z0 + z1 + 3$, $x=u + z0 + z1 + z2 + 4$.

Endpoints: $A=-u - z0 - z1 - z2 - 4$, $B=-u - z0 - z1 - 3$, $C0=-u - z0 - 2$, $D=0$, $E=-u - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=16 + 8\,z2 + 4\,z0 + 2\,z0\,z2 + 12\,u + 6\,u\,z2 + 2\,u\,z0 + u\,z0\,z2 + 2\,u^2 + u^2\,z2$$

$$H=8 + 8\,z2 + 2\,z0 + 2\,z0\,z2 + 6\,u + 6\,u\,z2 + u\,z0 + u\,z0\,z2 + u^2 + u^2\,z2$$

$$L=10 + 5\,z2 + 4\,z0 + 2\,z0\,z2 + 10\,u + 5\,u\,z2 + 2\,u\,z0 + u\,z0\,z2 + 2\,u^2 + u^2\,z2$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=14 + 7\,z2 + 8\,z0 + 4\,z0\,z2 + 18\,u + 9\,u\,z2 + 4\,u\,z0 + 2\,u\,z0\,z2 + 4\,u^2 + 2\,u^2\,z2$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 23: `e|y|c|x`

**[PROVED-HERE]** Blocks: `e|y|c|x`; variables: u, z0, z1, z2; `offset=0`, `shift=1`, all nonnegative integers.

Levels: $e=u + 1$, $y=u + z0 + 2$, $c=u + z0 + z1 + 3$, $x=u + z0 + z1 + z2 + 4$.

Endpoints: $A=-u - z0 - z1 - z2 - 4$, $B=-u - z0 - 2$, $C0=-u - z0 - z1 - 3$, $D=0$, $E=-u - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=28 + 10\,z2 + 13\,z1 + 2\,z1\,z2 + z1^2 + 6\,z0 + 2\,z0\,z2 + 2\,z0\,z1 + 20\,u + 7\,u\,z2 + 17/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 3\,u\,z0 + u\,z0\,z2 + u\,z0\,z1 + 3\,u^2 + u^2\,z2 + u^2\,z1$$

$$H=18 + 10\,z2 + 11\,z1 + 2\,z1\,z2 + z1^2 + 4\,z0 + 2\,z0\,z2 + 2\,z0\,z1 + 13\,u + 7\,u\,z2 + 15/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 2\,u\,z0 + u\,z0\,z2 + u\,z0\,z1 + 2\,u^2 + u^2\,z2 + u^2\,z1$$

$$L=19 + 7\,z2 + 10\,z1 + 2\,z1\,z2 + z1^2 + 6\,z0 + 2\,z0\,z2 + 2\,z0\,z1 + 17\,u + 6\,u\,z2 + 15/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 3\,u\,z0 + u\,z0\,z2 + u\,z0\,z1 + 3\,u^2 + u^2\,z2 + u^2\,z1$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=29 + 11\,z2 + 17\,z1 + 4\,z1\,z2 + 2\,z1^2 + 12\,z0 + 4\,z0\,z2 + 4\,z0\,z1 + 31\,u + 11\,u\,z2 + 14\,u\,z1 + 2\,u\,z1\,z2 + u\,z1^2 + 6\,u\,z0 + 2\,u\,z0\,z2 + 2\,u\,z0\,z1 + 6\,u^2 + 2\,u^2\,z2 + 2\,u^2\,z1$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 24: `e|y|x|c`

**[PROVED-HERE]** Blocks: `e|y|x|c`; variables: u, z0, z1, z2; `offset=0`, `shift=1`, all nonnegative integers.

Levels: $e=u + 1$, $y=u + z0 + 2$, $x=u + z0 + z1 + 3$, $c=u + z0 + z1 + z2 + 4$.

Endpoints: $A=-u - z0 - z1 - 3$, $B=-u - z0 - 2$, $C0=-u - z0 - z1 - z2 - 4$, $D=0$, $E=-u - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=18 + 11\,z1 + z1^2 + 4\,z0 + 2\,z0\,z1 + 13\,u + 15/2\,u\,z1 + 1/2\,u\,z1^2 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

$$H=8 + 9\,z1 + z1^2 + 2\,z0 + 2\,z0\,z1 + 6\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + u\,z0 + u\,z0\,z1 + u^2 + u^2\,z1$$

$$L=12 + 8\,z1 + z1^2 + 4\,z0 + 2\,z0\,z1 + 11\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + 2\,u\,z0 + u\,z0\,z1 + 2\,u^2 + u^2\,z1$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=18 + 13\,z1 + 2\,z1^2 + 8\,z0 + 4\,z0\,z1 + 20\,u + 12\,u\,z1 + u\,z1^2 + 4\,u\,z0 + 2\,u\,z0\,z1 + 4\,u^2 + 2\,u^2\,z1$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 25: `y|c|e|x`

**[PROVED-HERE]** Blocks: `y|c|e|x`; variables: u, z0, z1, z2; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $c=u + z0 + 1$, $e=u + z0 + z1 + 2$, $x=u + z0 + z1 + z2 + 3$.

Endpoints: $A=-u - z0 - z1 - z2 - 3$, $B=-u$, $C0=-u - z0 - 1$, $D=0$, $E=-u - z0 - z1 - 2$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=24 + 8\,z2 + 11\,z1 + 2\,z1\,z2 + z1^2 + 62/3\,z0 + 6\,z0\,z2 + 15/2\,z0\,z1 + z0\,z1\,z2 + 1/2\,z0\,z1^2 + 5\,z0^2 + z0^2\,z2 + z0^2\,z1 + 1/3\,z0^3 + 20\,u + 6\,u\,z2 + 15/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 10\,u\,z0 + 2\,u\,z0\,z2 + 2\,u\,z0\,z1 + u\,z0^2 + 4\,u^2 + u^2\,z2 + u^2\,z1 + u^2\,z0$$

$$H=16 + 8\,z2 + 9\,z1 + 2\,z1\,z2 + z1^2 + 44/3\,z0 + 6\,z0\,z2 + 13/2\,z0\,z1 + z0\,z1\,z2 + 1/2\,z0\,z1^2 + 4\,z0^2 + z0^2\,z2 + z0^2\,z1 + 1/3\,z0^3 + 14\,u + 6\,u\,z2 + 13/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 8\,u\,z0 + 2\,u\,z0\,z2 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z2 + u^2\,z1 + u^2\,z0$$

$$L=11 + 4\,z2 + 11/2\,z1 + z1\,z2 + 1/2\,z1^2 + 91/6\,z0 + 5\,z0\,z2 + 13/2\,z0\,z1 + z0\,z1\,z2 + 1/2\,z0\,z1^2 + 9/2\,z0^2 + z0^2\,z2 + z0^2\,z1 + 1/3\,z0^3 + 16\,u + 5\,u\,z2 + 13/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 9\,u\,z0 + 2\,u\,z0\,z2 + 2\,u\,z0\,z1 + u\,z0^2 + 4\,u^2 + u^2\,z2 + u^2\,z1 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=9 + 4\,z2 + 11/2\,z1 + z1\,z2 + 1/2\,z1^2 + 149/6\,z0 + 9\,z0\,z2 + 12\,z0\,z1 + 2\,z0\,z1\,z2 + z0\,z1^2 + 17/2\,z0^2 + 2\,z0^2\,z2 + 2\,z0^2\,z1 + 2/3\,z0^3 + 28\,u + 9\,u\,z2 + 12\,u\,z1 + 2\,u\,z1\,z2 + u\,z1^2 + 17\,u\,z0 + 4\,u\,z0\,z2 + 4\,u\,z0\,z1 + 2\,u\,z0^2 + 8\,u^2 + 2\,u^2\,z2 + 2\,u^2\,z1 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 26: `y|c|x|e`

**[PROVED-HERE]** Blocks: `y|c|x|e`; variables: u, z0, z1, z2; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $c=u + z0 + 1$, $x=u + z0 + z1 + 2$, $e=u + z0 + z1 + z2 + 3$.

Endpoints: $A=-u - z0 - z1 - 2$, $B=-u$, $C0=-u - z0 - 1$, $D=0$, $E=-u - z0 - z1 - z2 - 3$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=16 + 9\,z1 + z1^2 + 44/3\,z0 + 13/2\,z0\,z1 + 1/2\,z0\,z1^2 + 4\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 14\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + 8\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

$$H=8 + 7\,z1 + z1^2 + 26/3\,z0 + 11/2\,z0\,z1 + 1/2\,z0\,z1^2 + 3\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 8\,u + 11/2\,u\,z1 + 1/2\,u\,z1^2 + 6\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 2\,u^2 + u^2\,z1 + u^2\,z0$$

$$L=7 + 9/2\,z1 + 1/2\,z1^2 + 61/6\,z0 + 11/2\,z0\,z1 + 1/2\,z0\,z1^2 + 7/2\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 11\,u + 11/2\,u\,z1 + 1/2\,u\,z1^2 + 7\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=5 + 9/2\,z1 + 1/2\,z1^2 + 95/6\,z0 + 10\,z0\,z1 + z0\,z1^2 + 13/2\,z0^2 + 2\,z0^2\,z1 + 2/3\,z0^3 + 19\,u + 10\,u\,z1 + u\,z1^2 + 13\,u\,z0 + 4\,u\,z0\,z1 + 2\,u\,z0^2 + 6\,u^2 + 2\,u^2\,z1 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 27: `y|e|c|x`

**[PROVED-HERE]** Blocks: `y|e|c|x`; variables: u, z0, z1, z2; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $e=u + z0 + 1$, $c=u + z0 + z1 + 2$, $x=u + z0 + z1 + z2 + 3$.

Endpoints: $A=-u - z0 - z1 - z2 - 3$, $B=-u$, $C0=-u - z0 - z1 - 2$, $D=0$, $E=-u - z0 - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=24 + 8\,z2 + 11\,z1 + 2\,z1\,z2 + z1^2 + 62/3\,z0 + 6\,z0\,z2 + 15/2\,z0\,z1 + z0\,z1\,z2 + 1/2\,z0\,z1^2 + 5\,z0^2 + z0^2\,z2 + z0^2\,z1 + 1/3\,z0^3 + 20\,u + 6\,u\,z2 + 15/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 10\,u\,z0 + 2\,u\,z0\,z2 + 2\,u\,z0\,z1 + u\,z0^2 + 4\,u^2 + u^2\,z2 + u^2\,z1 + u^2\,z0$$

$$H=16 + 8\,z2 + 9\,z1 + 2\,z1\,z2 + z1^2 + 44/3\,z0 + 6\,z0\,z2 + 13/2\,z0\,z1 + z0\,z1\,z2 + 1/2\,z0\,z1^2 + 4\,z0^2 + z0^2\,z2 + z0^2\,z1 + 1/3\,z0^3 + 14\,u + 6\,u\,z2 + 13/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 8\,u\,z0 + 2\,u\,z0\,z2 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z2 + u^2\,z1 + u^2\,z0$$

$$L=13 + 5\,z2 + 8\,z1 + 2\,z1\,z2 + z1^2 + 91/6\,z0 + 5\,z0\,z2 + 13/2\,z0\,z1 + z0\,z1\,z2 + 1/2\,z0\,z1^2 + 9/2\,z0^2 + z0^2\,z2 + z0^2\,z1 + 1/3\,z0^3 + 16\,u + 5\,u\,z2 + 13/2\,u\,z1 + u\,z1\,z2 + 1/2\,u\,z1^2 + 9\,u\,z0 + 2\,u\,z0\,z2 + 2\,u\,z0\,z1 + u\,z0^2 + 4\,u^2 + u^2\,z2 + u^2\,z1 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=15 + 7\,z2 + 13\,z1 + 4\,z1\,z2 + 2\,z1^2 + 149/6\,z0 + 9\,z0\,z2 + 12\,z0\,z1 + 2\,z0\,z1\,z2 + z0\,z1^2 + 17/2\,z0^2 + 2\,z0^2\,z2 + 2\,z0^2\,z1 + 2/3\,z0^3 + 28\,u + 9\,u\,z2 + 12\,u\,z1 + 2\,u\,z1\,z2 + u\,z1^2 + 17\,u\,z0 + 4\,u\,z0\,z2 + 4\,u\,z0\,z1 + 2\,u\,z0^2 + 8\,u^2 + 2\,u^2\,z2 + 2\,u^2\,z1 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 28: `y|e|x|c`

**[PROVED-HERE]** Blocks: `y|e|x|c`; variables: u, z0, z1, z2; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $e=u + z0 + 1$, $x=u + z0 + z1 + 2$, $c=u + z0 + z1 + z2 + 3$.

Endpoints: $A=-u - z0 - z1 - 2$, $B=-u$, $C0=-u - z0 - z1 - z2 - 3$, $D=0$, $E=-u - z0 - 1$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=16 + 9\,z1 + z1^2 + 44/3\,z0 + 13/2\,z0\,z1 + 1/2\,z0\,z1^2 + 4\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 14\,u + 13/2\,u\,z1 + 1/2\,u\,z1^2 + 8\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

$$H=8 + 7\,z1 + z1^2 + 26/3\,z0 + 11/2\,z0\,z1 + 1/2\,z0\,z1^2 + 3\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 8\,u + 11/2\,u\,z1 + 1/2\,u\,z1^2 + 6\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 2\,u^2 + u^2\,z1 + u^2\,z0$$

$$L=8 + 6\,z1 + z1^2 + 61/6\,z0 + 11/2\,z0\,z1 + 1/2\,z0\,z1^2 + 7/2\,z0^2 + z0^2\,z1 + 1/3\,z0^3 + 11\,u + 11/2\,u\,z1 + 1/2\,u\,z1^2 + 7\,u\,z0 + 2\,u\,z0\,z1 + u\,z0^2 + 3\,u^2 + u^2\,z1 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=8 + 9\,z1 + 2\,z1^2 + 95/6\,z0 + 10\,z0\,z1 + z0\,z1^2 + 13/2\,z0^2 + 2\,z0^2\,z1 + 2/3\,z0^3 + 19\,u + 10\,u\,z1 + u\,z1^2 + 13\,u\,z0 + 4\,u\,z0\,z1 + 2\,u\,z0^2 + 6\,u^2 + 2\,u^2\,z1 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 29: `y|x|c|e`

**[PROVED-HERE]** Blocks: `y|x|c|e`; variables: u, z0, z1, z2; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $x=u + z0 + 1$, $c=u + z0 + z1 + 2$, $e=u + z0 + z1 + z2 + 3$.

Endpoints: $A=-u - z0 - 1$, $B=-u$, $C0=-u - z0 - z1 - 2$, $D=0$, $E=-u - z0 - z1 - z2 - 3$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=8 + 26/3\,z0 + 3\,z0^2 + 1/3\,z0^3 + 8\,u + 6\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

$$H=2 + 11/3\,z0 + 2\,z0^2 + 1/3\,z0^3 + 3\,u + 4\,u\,z0 + u\,z0^2 + u^2 + u^2\,z0$$

$$L=3 + 31/6\,z0 + 5/2\,z0^2 + 1/3\,z0^3 + 6\,u + 5\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=1 + 41/6\,z0 + 9/2\,z0^2 + 2/3\,z0^3 + 10\,u + 9\,u\,z0 + 2\,u\,z0^2 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

### Cell 30: `y|x|e|c`

**[PROVED-HERE]** Blocks: `y|x|e|c`; variables: u, z0, z1, z2; `offset=0`, `shift=0`, all nonnegative integers.

Levels: $y=u$, $x=u + z0 + 1$, $e=u + z0 + z1 + 2$, $c=u + z0 + z1 + z2 + 3$.

Endpoints: $A=-u - z0 - 1$, $B=-u$, $C0=-u - z0 - z1 - z2 - 3$, $D=0$, $E=-u - z0 - z1 - 2$, $F=0$.

**[COMPUTED] Exact ledger polynomials:**

$$N=8 + 26/3\,z0 + 3\,z0^2 + 1/3\,z0^3 + 8\,u + 6\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

$$H=2 + 11/3\,z0 + 2\,z0^2 + 1/3\,z0^3 + 3\,u + 4\,u\,z0 + u\,z0^2 + u^2 + u^2\,z0$$

$$L=3 + 31/6\,z0 + 5/2\,z0^2 + 1/3\,z0^3 + 6\,u + 5\,u\,z0 + u\,z0^2 + 2\,u^2 + u^2\,z0$$

**[PROVED-HERE] Certificate identity (expanded):**

$$3L-N=R_L=1 + 41/6\,z0 + 9/2\,z0^2 + 2/3\,z0^3 + 10\,u + 9\,u\,z0 + 2\,u\,z0^2 + 4\,u^2 + 2\,u^2\,z0$$

Every displayed monomial coefficient in this $R_L$ is nonnegative; omitted coefficients are zero. Hence this cell proves $N\le3L$.

## 3. Why the displayed polynomial identities are exact

**[PROVED-HERE]** On a fixed weak-order row, all endpoint bounds in the positive-part ledger are affine functions of the chamber variables and their relative order is fixed. The two crossed slices are sums of products of affine functions over a consecutive affine interval, and the tied slice is a sum of an affine function. Faulhaber expansion therefore gives polynomials of total degree at most three in $u,z_i$.

**[COMPUTED]** The generator solved the exact rational unisolvent interpolation problem for all monomials of total degree at most three (the sample set is all nonnegative vectors with coordinate sum at most three), then checked each resulting polynomial against the direct weighted-fiber enumeration on the full box $0\le u,z_i\le6$. It performed 102459 component checks and found no mismatch. The independent consumer does not use interpolation: it parses the stored coefficient lists, expands $3L-N$ coefficientwise, and directly enumerates every fiber on the same box.

**[PROVED-HERE]** Since a degree-$\le3$ polynomial that vanishes on the unisolvent interpolation set is zero, the exact coefficient rows are symbolic identities, not numerical guesses. The independent replay is an additional exact audit of the coefficient data and all endpoint/fiber translations.

## 4. Coefficientwise certificate conclusion

**[COMPUTED]** Across the 31 expanded residuals there are 391 nonzero residual monomials. The smallest nonzero residual coefficient is $1/2$; the largest is $31$; the replay found zero negative residual coefficients. It also found zero negative coefficients in the displayed $N,H,L$ polynomials.

**[PROVED-HERE]** For every nonnegative chamber point, $R_L\ge0$, so $N\le3L$. Since $H,L$ are nonnegative masses,
$$N\le3L\le3\max(H,L).$$

Therefore the target holds for all points of $\mathcal E_0$, and by §1.2 for all realizable $D=F$ instances.

## 5. Known realizable point and exact structural replay

**[COMPUTED]** For $m=2$, $I_p=[0,1]$, $I_q=I_r=[0,2]$, translate by $D=F=2$. Then
$$ (x,y,c,e,f)=(2,1,2,2,0),\qquad (A,B,C_0,D,E,F)=(-2,-1,-2,0,-2,0).$$

It is cell 0, pattern `y|xce`, with $(u,z_0)=(1,0)$. Direct weighted fibers give $N=18,H=6,L=11$, and the certificate residual is $3L-N=15$.

The independent structural check constructs the five-element poset from $c_1<c_2$, $p<q$, $p<r$, and the endpoint relations. It reports acyclic `True`, $q\parallel r$ `True`, height $2$, connected incomparability graph `True`, and 18 linear extensions. Thus this is a realizable boundary witness and not a counterexample.

## 6. Independent replay/data and exact output

**[COMPUTED]** The replay consumer is standalone with respect to the generator: it uses only Python integer loops, exact `Fraction` coefficient parsing, the JSON coefficient lists, and direct transitive-closure/permutation checks for the known point. It reports:

```text
DATA_SHA256 7aad8e7378dfe5475ba1dc3b8283e8250adf64dafe3359a0a0460b23c6288a5a
PATTERN_COUNT 31
PATTERN_COVERAGE_BOX 2304
PATTERN_HIT_COUNTS 0:36 1:28 2:28 3:28 4:56 5:56 6:56 7:56 8:56 9:84 10:84 11:84 12:84 13:84 14:84 15:56 16:56 17:56 18:56 19:70 20:70 21:70 22:70 23:70 24:70 25:126 26:126 27:126 28:126 29:126 30:126
IDENTITY_EXPANSIONS 31
IDENTITY_RESIDUAL_TERMS 391
NEGATIVE_RESIDUAL_COEFFICIENTS 0
NEGATIVE_NHL_COEFFICIENTS 0
DIRECT_BOX_CHECKS 102459
BOUNDARY_EQUALITY_CHECKS 328
E_EQUALS_1_DOMAIN_ROWS 288
KNOWN_POINT x=2 y=1 c=2 e=2 f=0 parameters=pattern0(u=1,z0=0) N=18 H=6 L=11
KNOWN_POSET {'acyclic': True, 'q_parallel_r': True, 'height': 2, 'incomparability_connected': True, 'linear_extensions': 18, 'ledger': (18, 6, 11)}
ALL_CHECKS_PASS True
```

The exact files and hashes consumed/generated in this session are:

| file | SHA-256 |
|---|---|
| `outputs/data/te21_D_eq_F_facet_atlas_20260818.json` | `7aad8e7378dfe5475ba1dc3b8283e8250adf64dafe3359a0a0460b23c6288a5a` |
| `outputs/code/generate_te21_D_eq_F_facet_atlas_20260818.py` | `8679af787466d8e8927d839abd048fde31d7c869491f2b0cf0b873910e70bcf4` |
| `outputs/code/replay_te21_D_eq_F_facet_atlas_20260818.py` | `fce41ac04f3d13a50cb7ad099d7ee49d9067c7acdd0c529ce3daae66fa31a81d` |
| `outputs/artifacts/te21_D_eq_F_facet_atlas_20260818/replay_report.txt` | `50303d6d5fc9d684d63723803d9bffbde719db2fb15f173ee3a5359256a0a791` |

The replay boundary tests include all $2^d$ zero/one vectors in every cell (328 cases), all 288 finite-box rows with $e=1$, and the all-zero lowest-level face in each of the 31 cells. The finite coverage box $0\le x,y,c,e\le8$ contains 2304 envelope points and hits every pattern; the infinite coverage is the parameterization proof in §2, not an extrapolation from this box.

## 7. Merger interface with the certified $f\ge1$ atlas

**[ARGUED]** Use the existing atlas without rederivation:

| regime | normalized endpoints | certificate artifact |
|---|---|---|
| $f\ge1$ | $(A,B,C_0,D,E,F)=(-x,-y,-c,0,-e,1+v)$, $v\ge0$ | `outputs/artifacts/gated_te21_chamber_atlas_20260817/atlas.md` |
| $f=0$ | $(A,B,C_0,D,E,F)=(-x,-y,-c,0,-e,0)$, $e\ge1$ | this artifact |

The shared interface is the same closed-fiber ledger $W=1+\mathbf1_{j=k}$, the same strict-tail definitions $H=U_p(A)$ and $L=L_q(D)$, and the same WLOG convention $D\le F$. The dispatcher is simply `if f==0 use this 31-cell atlas; if f>=1 use the existing 31-cell/62-certificate atlas`. The regimes are disjoint and their union is every normalized nonnegative $f$ allowed by the endpoint consequence $D\le F$.

Existing dependency hashes, recomputed in-session, are:

- existing atlas markdown: `3541901a46c6e9603933d95546d3adb075df15570e6cc6134c7a67ed2c8777a7`;
- existing atlas JSON: `59e2b841ce2cb653d900a73092165f1b78547f4bf6023c4b04adf677a878174d`;
- existing atlas code: `415b3d1260a3a767ad89f0bf17113312ac4b224f1913860124a8d22df53d59ca`.

## 8. Final status

**[PROVED-HERE]** No counterexample was found or needed. The omitted facet is closed by the stronger exact inequality $N\le3L$ on the full 31-cell containment envelope. No unfinished lemma is used in the facet proof beyond the attached exact guarded-V ledger and realizability guards, which are explicitly treated as dependencies.
