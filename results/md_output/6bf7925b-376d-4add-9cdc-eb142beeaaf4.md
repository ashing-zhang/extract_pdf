WHEN ARE THERE CONTINUOUS CHOICES FOR THE MEAN
VALUE ABSCISSA?
9102 nuJ 5  ]AC.htam[  1v62020.6091:viXra
DAVID LOWRY-DUDA AND MILES WHEELER
Abstract. The mean value theorem of calculus states that, given a differ-
entiable function f on an interval [a,b], there exists at least one mean value
abscissa c such that the slope of the tangent line at c is equal to the slope of
the secant line through (a,f(a)) and (b,f(b)). In this article, we study how
the choices of c relate to varying the right endpoint b. In particular, we ask:
When we can write c as a continuous function of b in some interval?
Drawing inspiration from graphed examples, we first investigate this ques-
tion by proving and using a simplified implicit function theorem. To handle
certain edge cases, we then build on this analysis to prove and use a simpli-
fied Morse’s lemma. Finally, further developing the tools proved so far, we
conclude that if f is analytic, then it is always possible to choose mean value
abscissae so that c is a continuous function of b, at least locally.
1. Introduction and Statement of the Problem.
The mean value theorem is one of the truly fundamental theorems of calculus.
It says that if f is a differentiable function defined on a closed interval [a,b], then
there is at least one c in the open interval (a,b) such that
f(b) f(a)
′
(1) − = f (c).
b a
−
We call c a mean value abscissa for f on [a,b]. Looking at a graph y = f(x) as in
Figure 1, the left hand side of (1) is the slope of the secant line from (a,f(a)) to
(b,f(b)), while the right hand side is the slope of the tangent line passing through
(c,f(c)). Observe that there can be multiple choices of c; in the first graph in
′
Figure 1 we could have chosen either c or c .
In this article we are interested in how the set of mean value abscissae c changes as
we vary one of the endpoints of the interval, say the right endpoint b. In particular,
we are interested in the following problem: Suppose c = c is our favorite mean
0
value abscissa for a = a and b = b . If b changes slightly, can we also change c
0 0
slightly so that (1) is still satisfied? In other words, is there a locally continuous
choice c = C(b) of the mean value abscissa? For example, in the right-hand
graph in Figure 1, we consider the new value b . Here, it appears that the small
new
′ ′
change from b to b corresponds to small changes from c to c and c to c
new new new
— is this always possible?
2. Some examples.
To get a better feel for the problem we have set out for ourselves, let’s graph
some functions and their mean value abscissae. To make our life simpler, we will
stick to examples with a = a = 0 and f(a ) = f(b ) = 0. Then the left hand
0 0 0
side of (1) is zero when a = a and b = b , and so any corresponding mean value
0 0
1

2 DAVID LOWRY-DUDA AND MILES WHEELER
2 2
1 1
f 0 f 0
− −
1 1
− −
2 2
a b a b new
′
0 c 1 c′ 2 0 c new 1 c new 2
x x
Figure 1. An illustration of the mean value theorem on the func-
tion f(x) = x3 3x2 + 2x. The straight lines are the secant lines.
−
In each graph, the end-points of the secant line and two mean value
abscissae are indicated by points on the curve. Dashed lines from
each point indicate corresponding x-values.
′
abscissa c = c has to be a critical point where f (c ) = 0. This may seem like a
0 0
lot of assumptions, but in fact if someone hands us a more general function f we
can always consider the related function
f(b ) f(a )
0 0
g(x) = f(x) − (x a ) + f(a ) ,
0 0
− b a −
(cid:16) 0 0 (cid:17)
−
which satisfies g(a ) = g(b ) = 0. Both f and g have the same solutions to the
0 0
mean value condition (1).
Consider the parabola at the left of Figure 2. There is only one choice of c :
0
the vertex. When we slightly increase b to b , we have to slightly increase c to
0 1 0
c . Similarly if we decrease b to b , then we have to decrease c to c . Plotting
1 0 2 0 2
the mean value abscissae c for each b, we get the picture at the right of Figure 2.
Looking at the figure, c seems to be a continuous function of b, and indeed in
this case we can solve (1) explicitly to get c = b/2. In particular, the ratio c/b is
constant; for more on the class of functions with this property, see [1].
Next consider the more complicated graph at left in Figure 3. There are now two
critical points. One is a local maximum, and the behavior near this point is very
similar to the behavior near the vertex of the parabola. The second one, which we
have labeled as c , is a non-extremal critical point (it is neither a local maximum
0
nor a local minimum). Suppose that b is just a bit bigger than b . Then the slope
1 0
of the secant line which appears on the right hand side of (1) is < 0. When c is
′
close to c , on the other hand, the right hand side f (c) of (1) is 0. There is no
0
≥
solution to (1) without choosing c far away from c .
0
3. The implicit function theorem.
3.1. Implicit equations. In the last section, we saw that the set of solutions (b,c)
of (1) can look quite complicated. On the right of Figure 3, for instance, c is not
a function of b (the curve fails the “vertical line test”) and b is also not a function

|    | None   | None   | None   |
|:---|:-------|:-------|:-------|
|    | a      |        | b      |

WHEN ARE THERE CONTINUOUS CHOICES FOR THE MEAN VALUE ABSCISSA? 3
2
3
0
f c 2
−
2
(b 1,c 1)
1 (b 0,c 0)
(b 2,c 2)
−
4
a c b b b
0 0 2 0 1
0
c c
2 1
0 1 2 3 0 1 2 3
x b
Figure 2. Left: the parabola y = x2 + 2x. Three pairs of
−
points are shown: (b ,c ), (b ,c ), and (b ,c ). For each b , the
0 0 1 1 2 2 i
corresponding c is a mean value abscissa on the interval [a ,b ].
i 0 i
Right: the graph of all mean value abscissae as a function of b
(where a = 0 is fixed); b is on the horizontal axis, and c = b/2 is
0
on the vertical axis. Points corresponding to the three pairs on the
left are noted. In the mean value theorem, b > c, and we represent
this by shading the region where c b.
≥
of c (the curve fails the “horizontal line test”). This is possible because (1) is an
implicit equation.
Implicit equations show up all over the place in mathematics, for instance in
geometry; x2 + y2 = 1 is the equation for the circle with radius one centered
at the origin, while x2 + 4xy + y2 = 2 is the equation for a certain hyperbola.
By subtracting off the right hand side, we can write any implicit equation in two
variables as
(2) F(x,y) = 0
for some function F. It’s often tempting to try and solve an implicit equation for
one of the variables, and indeed that’s indeed how we got the formula c = b/2
for the example on the right of Figure 2. When the equation gets more complex,
though, like it is in Figure 3, this method becomes very tedious and is quite often
impossible!
3.2. The implicit function theorem. Thankfully, calculus offers us a powerful
tool, called the implicit function theorem, to help us understand implicit equations.
The intuition behind the theorem is the following: Suppose that we have found
one solution (x ,y ) to (2), and are only interested in solutions of (2) nearby this
0 0
initial solution. If the function F is differentiable, then for (x,y) (x ,y ) we can
0 0
≈
approximate F as
(3) F(x,y) F(x ,y ) + F (x ,y )(x x ) + F (x ,y )(y y ),
0 0 x 0 0 0 y 0 0 0
≈ − −
where the subscripts on F are partial derivatives. This is a first-order Taylor
approximation of F, a two-variable version of the tangent-line approximation for

|    | None   | None   | None   | None   | None   | None   |
|:---|:-------|:-------|:-------|:-------|:-------|:-------|
|    | a0     |        | c0     |        | b2     | b0 b1  |

|    |    |         |
|:---|:---|:--------|
|    |    | (b      |
|    | (b | (b0,c0) |
|    |    | 2,c2)   |

4 DAVID LOWRY-DUDA AND MILES WHEELER
1.0
3
0.5
f 0.0 c 2
− 0.5
(b 0,c 0)
1
− 1.0
a c b
0 0 0
− 1.5 0
b
0 1 2 3 0 1 2 3 4
x b
Figure 3. Left: the graph of a function with an inflection point.
The point (1,1) is a mean value abscissa on the interval [0,3], but
there is no continuous extension of this solution to a neighborhood
of b . The straight line is the secant line corresponding to the
0
interval [a ,b ]. Right: the graph of all mean value abscissae
0 1
as a function of b, as in the previous Figure. The behavior is
substantially more complicated. At the point (b ,c ), we observe
0 0
that c is not a function of b.
functions of a single variable. Plugging (3) into the equation (2) that we are trying
to solve and using F(x ,y ) = 0, we get
0 0
(4) F (x ,y )(x x ) + F (x ,y )(y y ) 0.
x 0 0 0 y 0 0 0
− − ≈
While (4) is only approximately true, it’s advantage is that it’s a linear equation.
In particular, if F (x ,y ) = 0, then we can try to “solve for y”, giving the approx-
y 0 0
6
imation
F (x ,y )
x 0 0
(5) y = Y (x) y (x x ).
0 0
≈ − F (x ,y ) −
y 0 0
The implicit function theorem says that the conclusion of this intuitive argument
is nearly correct: as long as F(x ,y ) = 0 and F (x ,y ) = 0, we can indeed solve
0 0 y 0 0
6
F(x,y) = 0 for y when (x,y) is close to (x ,y ).
0 0
Theorem 1 (Implicit Function Theorem). Suppose that F = F(x,y) is a contin-
uously differentiable function and that at some point (x ,y ) we have
0 0
(6) F(x ,y ) = 0 and F (x ,y ) = 0.
0 0 y 0 0
6
Then there exist ε > 0, δ > 0, and a continuously differentiable function Y (x) such
that the implicit equation F(x,y) = 0 is equivalent to the explicit equation y = Y (x)
whenever x x < δ and y y < ε.
0 0
| − | | − |
3.3. Proof of the implicit function theorem. The implicit function theorem
above is an existence theorem: it says there exists a function Y = Y (x) with some
special properties. Like many of the existence theorems in calculus, the implicit
function theorem has a nice proof using the contraction mapping principle. The

|    |     |      |    |    |
|:---|:----|:-----|:---|:---|
|    |     |      |    |    |
|    | (b0 | ,c0) |    |    |
|    |     |      |    |    |

WHEN ARE THERE CONTINUOUS CHOICES FOR THE MEAN VALUE ABSCISSA? 5
implicit function theorem presented here is a simplified version, but the proofs of
more general versions share have the same basic outline; see, for instance, [6, 13].
§
The contraction mapping principle, which is also called Banach’s fixed-point
theorem, concerns equations of the form
(7) y = K(y), y in I
where I = [A,B] is a closed interval. We call (7) a “fixed-point equation” because
it says that the point y is “fixed” (or unchanged) when we apply the function K to
it. The theorem assumes that the function K satisfies
′ ′ ′
(8) K(y) K(y ) ρ y y for all y,y in I
| − | ≤ | − |
′
for some constant ρ < 1. If y,y are two points a distance d apart, then (8) says
′
that the distance between their images K(y),K(y ) is at most ρd. Since ρd < d,
the points are closer together after we apply K, and so we call K a contraction.
Theorem 2 (Contraction Mapping Principle). Suppose that the function K is
defined on a closed interval I where it satisfies (8) for some constant ρ < 1. If
K(y) lies in I for every y in I, then the fixed-point equation (7) has a unique
∗
solution y .
′
Proof. First we show that solutions of (7) are unique. Suppose that y and y both
′
solve (7), so that they satisfy y = K(y) and y = K(y ). Then by (8) we see that
′ ′ ′
y y = K(y) K(y ) ρ y y .
| − | | − | ≤ | − |
′
Since ρ < 1, this is only possible if y = y .
Having shown uniqueness of a potential solution, we now show that (7) has
∗
a solution y . Choose any point y in I and define the sequence y ,y ,y ,...
0 1 2 3
recursively by
(9) y = K(y ).
n+1 n
Since K sends points in I to points in I, this definition makes sense and we can
prove by induction that y lies in I for all n. We will show that lim y exists,
n n→∞ n
∗
and that it is the fixed point y we are looking for.
By repeatedly using (8) and (9), we can estimate the distance between successive
terms y and y in our sequence:
n+1 n
y y = K(y ) K(y )
n+1 n n n−1
| − | | − |
ρ y y
n n−1
≤ | − |
(10) = ρ K(y n−1) K(y n−2)
| − |
ρ2 y y
n−1 n−2
≤ | − |
ρn−1
y y .
1 0
≤ ··· ≤ | − |

6 DAVID LOWRY-DUDA AND MILES WHEELER
Since ρ < 1, the right hand side converges to zero very quickly as n . If n > m,
→ ∞
we can then repeatedly use (10) to estimate the difference between y and y :
n m
y y = (y y ) + (y y ) + + (y y )
n m n n−1 n−1 n−2 m+1 m
| − | | − − ··· − |
y y + y y + + y y
n n−1 n−1 n−2 m+1 m
≤ | − | | − | ··· | − |
y y (ρn−1 + ρn−2 + + ρm)
1 0
≤ | − | ···
1 ρn
= y y ρm −
1 0
| − | 1 ρ
−
ρm
< y y .
1 0
| − |1 ρ
−
Here in the second step we have used the triangle inequality, and in the second-
to-last step we have used the formula for the (partial) sum of a geometric series.
As before the right hand side converges to 0 as m 0, which now shows that the
→∗
sequence y is Cauchy. In particular, the limit y = lim y exists. Since
n n→∞ n
{ } ∗
each y lies in the closed interval I, the same is true for the limit y .
n
Finally, we note that (8) implies that K is continuous. Taking the limit of the
∗ ∗ ∗ (cid:3)
recurrence (9) as n , we therefore get y = K(y ), i.e. that y solves (7).
→ ∞
To use Theorem 2 to prove Theorem 1, we first rewrite F(x,y) = 0 as a fixed-
point equation y = K(y;x) for y. When x is close to x and I is a small interval
0
centered at y , we will then show that this K is a contraction mapping satisfying
0
the hypotheses of Theorem 2. Here the notation K(y;x) is to remind us that y is
the main variable while x is a parameter.
To keep things simple, we only prove the implicit function theorem for the special
case x = y = 0. It’s easy to prove the general case from this specific one by
0 0
considering the shifted function G(x,y) = F(x + x,y + y). The inspiration for
0 0
the proof is our informal argument which lead to (5). This argument started with
the Taylor expansion (3), but to make it rigorous we start with an exact version of
that formula:
(11) F(x,y) = F (0,0)x + F (0,0)y + r(x,y).
x y
Here r(x,y) is the remainder term, which is small when (x,y) is close to (0,0), and
we have used that x = y = 0 and F(x ,y ) = F(0,0) = 0. To devise a mapping
0 0 0 0
K, we set F(x,y) = 0 and do some algebra to bring the y to the left hand side to
get
(0,0)−1
(12) y = F F (0,0)x + r(x,y) .
y x
−
(cid:16) (cid:17)
Solving (11) for r(x,y) and plugging into (12), things simplify a bit and we get
(0,0)−1F(x,y).
(13) y = y F
y
−
We see that (13) is true if and only if F(x,y) = 0. What we have gained, though,
is that (13) gives a fixed-point equation for y, and so we can hope to solve it for y
by applying Theorem 2 with
(0,0)−1F(x,y).
(14) K = K(y;x) = y F
y
−
We apply Theorem 2 with ρ = 1/2 and I = [ ε,ε] for some small number ε > 0
−
which we still have to determine. This ensures that we are only considering y-values
which are close to y = 0. We will also restrict ourselves to x-values which are close
0

WHEN ARE THERE CONTINUOUS CHOICES FOR THE MEAN VALUE ABSCISSA? 7
to x = 0, say x in [ δ,δ] for some other small number δ > 0. The hypotheses of
0
−
Theorem 2 will therefore be met as long as
(15) K(y;x) ε for x δ, y ε,
| | ≤ | | ≤ | | ≤
(16) K(y;x) K(y′ ;x) 1 y y′ for x δ, y , y′ ε.
| − | ≤ 2| − | | | ≤ | | | | ≤
The second inequality (16) is the contraction condition (8), while the first (15)
guarantees that K(y;x) lies in I whenever y does.
We’ll prove (16) using, of all things, the mean value theorem. Differentiating
with respect to y we get
(0,0)−1F
K (y;x) = 1 F (x,y).
y y y
−
It’s clear that at (0,0), the right hand side is 0. Since F is continuous, we can pick
y
ε > 0 small enough that the right hand side is bounded by 1/2 whenever x , y ε.
′ | | | | ≤
Now suppose that x , y , y ε. Applying the mean value theorem to K on the
x
| | | |′ | | ≤
interval between y and y , we get that
(17) K(y′ ;x) K(y;x) = K (c;x) y′ y 1 y′ y
y
| − | | || − | ≤ 2| − |
′
for some point c between y and y . This shows (16).
We still need to show (15). As long as x , y ε, we can use (16) to estimate
| | | | ≤
K(y;x) K(y;x) K(0;x) + K(0;x)
| | ≤ | − | | |
(18) 1 y + K(0;x)
≤ 2| | | |
1ε + K(0;x) .
≤ 2 | |
Since K(0;x) is a continuous function of x and K(0;0) = 0, there exists a δ > 0
so that K(0;x) ε/2 whenever x δ. Picking δ smaller if necessary so that
| | ≤ | | ≤
δ ε, (18) finally implies that K(y;x) 1ε + 1ε = ε whenever x δ and
≤ | | ≤ 2 2 | | ≤
y ε.
| | ≤
Now that we have finished proving (15) and (16), we can apply Theorem 2 to
guarantee that the fixed point equation y = K(y;x) has a unique solution y =
Y (x) in [ ε,ε] for each x in [ δ,δ]. Since the fixed-point equation y = K(y;x) is
− −
equivalent to F(x,y) = 0, this completes the proof of the theorem except for the
claim that Y is a continuously differentiable function.
To see that Y (x) is continuous, we write
′ ′ ′
Y (x ) Y (x) = K(Y (x );x ) K (Y (x);x)
x
| − | | − |
′ ′ ′ ′
K(Y (x );x ) K(Y (x);x ) + K(Y (x);x ) K(Y (x);x) .
≤ | − | | − |
By (17), the first term on the right hand side is bounded by 1 Y (x′ ) Y (x) .
2| − |
Rearranging, this shows that
′ ′
Y (x ) Y (x) 2 K(Y (x);x ) K(Y (x);x) .
| − | ≤ | − |
The continuity of Y then follows from the continuity of K(y;x) as a function of x.
Next we show that Y is continuously differentiable and calculate its derivative.
′
If we knew ahead of time that Y was differentiable, then we could solve for Y (x)
by differentiating F(x,Y (x)) = 0 using the chain rule. Since we do not know yet
that Y is differentiable, we instead look at the difference quotient
F(x + h,Y (x + h)) F(x,Y (x))
0 = − .
h

8 DAVID LOWRY-DUDA AND MILES WHEELER
Using the fundamental theorem of calculus in a clever way, we rewrite the numerator
of this difference quotient as
0 = F(x + h,Y (x + h)) F(x,Y (x))
−
1
d
= F(x + th,tY (x + h) + (1 t)Y (x))dt
Z dt −
0
1 1
= h F dt + (Y (x + h) Y (x)) F dt,
x y
Z − Z
0 0
where the arguments of both F and F are (x+ty,tY (x+h)+(1 t)Y(x)). Notice
x y
−
that the chain rule has caused a (Y (x + h) Y (x)) to appear. We rearrange this
−
into an expression for the difference quotient
−1
1 1
Y (x + h) Y (x)
− = F dt F dt.
y x
h −(cid:20)Z (cid:21) Z
0 0
Since F (0,0) = 0, for h small enough the integral of F will not vanish, and so it
y y
6
is valid to divide by it.
′
Now we take the limit as h 0. On the left hand side, this gives Y (x) directly.
→
On the right hand side, we have to pass the limit inside the integrals. Since (x +
th,tY (x + h) + (1 t)Y (x)) converges uniformly to (x,Y (x)) as h 0, this is
− →
justified and we get
F (x,Y (x))
′ x
(19) Y (x) = .
−F (x,Y (x))
y
This proves that Y is differentiable. Since Y is continuous and F is continuously
differentiable, the right hand side of (19) is continuous, and so Y is in fact continu-
ously differentiable. Looking at (19), we also see that this justifies the approximate
formula (5) as we had hoped!
By repeatedly differentiating (19), we discover that if F is k-times continuously
differentiable, then so is Y . We record this observation as a corollary to the proof
of Theorem 1.
′
Corollary 3. In Theorem 1, the derivative Y is given by (19). If F is k-times
continuously differentiable, then Y is k-times continuously differentiable.
3.4. Application to the Mean Value Abscissa. With the implicit function
theorem in hand, we are now ready to investigate the possibility of determining
when there exist locally continuous choices of the mean value abscissa c in (1). The
first step is to rewrite (1) as F(b,c) = 0 where
f(b) f(a)
′
(20) F(b,c) = − f (c).
b a −
−
From now on we assume that f is twice continuously differentiable, in which case
F is once continuously differentiable.
Suppose that c is a mean value abscissa corresponding to b , i.e. that F(b ,c ) =
0 0 0 0
0. A quick computation shows that
′ ′
f (b ) f (c )
0 0 ′′
F (b ,c ) = − , F (b ,c ) = f (c ).
b 0 0 c 0 0 0
b a −
0
−
′′ ′′
Thus F (b ,c ) = 0 is true exactly when f (c ) = 0. And if f (c ) = 0, then by
c 0 0 0 0
6 6 6
Theorem 1 there exists ε > 0, δ > 0, and a continuously differentiable function C(b)
so that F(b,c) = 0 is equivalent to c = C(b) whenever c c < ε and b b < δ.
0 0
| − | | − |

WHEN ARE THERE CONTINUOUS CHOICES FOR THE MEAN VALUE ABSCISSA? 9
Although we have focused on the question of when the mean value abscissa c
can be written as a continuous function of the right endpoint b, we also have the
data for the converse question: When is the right endpoint b a function of the mean
value abscissa c? By Theorem 1, b can be written as a function of c near (b ,c )
0 0
′ ′
when F (b ,c ) = 0, or equivalently when f (b ) = f (c ).
b 0 0 0 0
6 6
In total we have proved the following theorem.
Theorem 4. Let f be a twice continuously differentiable function, fix an interval
[a ,b ], and let c be a mean value abscissa for f on [a ,b ].
0 0 0 0 0
′′
(a) Suppose that f (c ) = 0. Then there is a continuously differentiable func-
0
6
tion C(b) so that
f(b) f(a)
′
− = f (C(b))
b a
−
for all b close to b . There are no other solutions (b,c) of (1) close to
0
(b ,c ).
0 0
′ ′
(b) Suppose that f (b ) = f (c ). Then there is a continuously differentiable
0 0
6
function B(c) so that
f(B(c)) f(a)
′
− = f (c)
B(c) a
−
for all c close to c . There are no other solutions (b,c) of (1) close to
0
(b ,c ).
0 0
Remark. Given an initial solution (b ,c ), our proof of Theorem 4 is constructive
0 0
in that iterating the contraction map from the proof Theorem 1 actually gives us
an algorithm for approximating B(c) or C(b) to any order of accuracy.
This theorem gives perspective on Figure 3. The mean value abscissa in that
′′
figure was at an inflection point, where f (c ) = 0, and so Theorem 4a is inconclu-
0
sive about whether we can write c = C(b). Looking at the figure it appears that
′ ′
we cannot. On the other hand f (b ) < f (c ) = 0, and so Theorem 4 implies that
0 0
we can write b = B(c).
4. The Morse Lemma.
We have now shown that there exist continuous choices of c = C(b) around
′′
those mean value abscissae such that f (c ) = 0. Conversely, we’ve shown that
0
6 ′ ′
when there is a mean value abscissa c such that f (b ) = f (c ), then b can be
0 0
6
written as a continuous function in a neighborhood of c .
0
′′ ′ ′
But what if both f (c ) = 0 and f (b ) = f (c )? As before, we return to
0 0 0
pictorial investigation. Fortunately, these are two strong constraints and we quickly
identify interesting aspects from graphs.
For ease, we suppose again that f(a ) = f(b ) = 0, and we now suppose that
0 0
′ ′ ′′
f (c ) = f (b ) = f (c ) = 0. In Figure 4, we examine three different functions
0 0 0
′′ ′′
f: each satisfiesf (c ) = 0, but f (b) is positive on the left, zero in the middle,
0
and negative on the right. We’ve named these three values of b as b , b , and
m i
b (according to whether b is a minimum, an inflection point, or a maximum,
M
respectively).
Examining the top left graph of Figure 4, we observe that in a small neighbor-
hood of c , all tangent lines have nonnegative slope. Similarly, for all b in a small
0

10 DAVID LOWRY-DUDA AND MILES WHEELER
2 2 2
1 1 1
f f f
0 0 0
−1 a c b −1 a c b −1 a c b
0 0 m 0 0 i 0 0 M
0 1 2 3 0 1 2 3 0 1 2 3
x x x
3 3 3
c 2 c 2 c 2
1 1 1
(b i,c 0) (b M,c 0)
(b m,c 0)
0 0 0
0 1 2 3 0 1 2 3 0 1 2 3
b b b
Figure 4. Top: Three graphs of functions f with an interval
and corresponding mean value abscissa indicated. In each graph,
′′ ′′
f (c ) = 0. In the left graph, f (b ) > 0. In the middle graph,
0 m
′′ ′′
f (b ) = 0. In the right graph, f (b ) < 0. Bottom: Below each
i M
graph is a plot of all mean value abscissae as a function of b, as
in previous figures. In the first graph, there appear to be multiple
choices of continuous function c(b). In the second graph, there is a
continuous extension on an interval with b as an endpoint. In the
i
third graph, the initial solution is completely isolated.
neighborhood around b , the secant lines from (0,0) to (b,f(b)) have nonnegative
m
′
slope. Qualitatively, it appears that for b just a little less than b , we could vary c
m
to match slopes. But which direction should c be moved? We can see this apparent
choice of direction in the mean value abscissa graph at bottom left: near (b ,c ),
m 0
the graph resembles an X.
′′
This reveals a key difference to the situation when f (c) = 0. In both the
6
implicit function theorem and Theorem 4, the resulting implicitly defined functions
are unique. This is due to the uniqueness of the fixed points in the contraction
mapping principle. But here, it appears that sometimes there are multiple different
continuous choices of c(b) — that is, if there are any at all.
In the top right graph of Figure 4, we see that in a small neighborhood of c , all
0
tangent lines again have nonnegative slope. But in a small neighborhood around
b , the secant lines from (0,0) to (b,f(b)) all have nonpositive slope. Thus there
M
is no hope to extend c to a function to a larger neighborhood at all. We recognize
this in the mean value abscissa graph below by seeing that (b ,c ) is an isolated
M 0
point.

|    | None   | None   | None   |
|:---|:-------|:-------|:-------|
|    | a0     | c0 bm  |        |

|    | None   | None   | None   |
|:---|:-------|:-------|:-------|
|    | a0     | c0 bi  |        |

|    | None   | None   | None   |
|:---|:-------|:-------|:-------|
|    | a0     | c0 bM  |        |

|    |    | x   |    |     |
|:---|:---|:----|:---|:----|
|    |    |     |    |     |
|    |    |     |    |     |
|    |    |     | (b | m,c |
|    |    |     |    |     |

|    |    | x   |    |      |
|:---|:---|:----|:---|:-----|
|    |    |     |    |      |
|    |    |     |    |      |
|    |    |     | (b | i,c0 |
|    |    |     |    |      |

|    |    | x   |    |     |
|:---|:---|:----|:---|:----|
|    |    |     |    |     |
|    |    |     |    |     |
|    |    |     | (b | M,c |
|    |    |     |    |     |

WHEN ARE THERE CONTINUOUS CHOICES FOR THE MEAN VALUE ABSCISSA? 11
The behavior in the top center graph, near b , is a bit more delicate. Here, in
i
a small neighborhood of c , all tangent lines have nonpositive slope. For b just to
0
the left of b , the secant lines from (0,0) to (b,f(b)) have nonpositive slope, and
i
so it qualitatively appears that it might be possible to associate points near c with
matching slopes. But for b just to the right of b , the secant lines all have positive
i
slope, which cannot be matched to slopes of points in a neighborhood of c.
These examples indicate a wider variety of behavior, and it’s not at all obvious
what the general rule should be. We cannot hope to directly apply an implicit
function theorem without some significant changes.
As with our investigation of the implicit function theorem, let us start with the
Taylor expansion of F(b,c) at (b ,c ). As F(b ,c ) = F (b ,c ) = F (b ,c ) = 0, all
0 0 0 0 b 0 0 c 0 0
the terms in this expansion are at least quadratic. For simplicity, let’s assume that
two of the quadratic terms are nonzero, more specifically that the partial derivatives
F (b ,c ) = 0 and F (b ,c ) = 0. In this case, there is a result called the Morse
bb 0 0 cc 0 0
6 6
lemma which is perfectly tailored for our situation! A simple version of the Morse
lemma is the following.
Lemma 5 (Morse lemma). Let G = G(x,y) be a three-times continuously differ-
entiable function and suppose that G(0,0) = G (0,0) = G (0,0) = 0 but that
x y
(21) G (0,0)G (0,0) (G (0,0))2 = 0.
xx yy xy
− 6
Then in a neighborhood of the origin there is a change of coordinates (x,y) (u,v)
7→
so that
(22) G(x,y) = u2 v2.
± ±
The number of minus signs on the right hand side of (22) is called the Morse
index of G at 0. It is independent of the particular choice of coordinates (u,v), and
is one of the basic ingredients in Morse theory [3]. By a “change of coordinates”
(x,y) (u,v), we mean that u and v can be written as continuously differentiable
7→
functions of (x,y), while at the same time x and y can be written as continuously
differentiable functions of (u,v). We also require that (0,0) (0,0).
7→
Remark. Those familiar with multivariable calculus might recognize the conditions
of the Morse lemma as an alternate way of saying that the gradient of G vanishes
at the origin, but the Hessian matrix is invertible there. A full proof of the Morse
lemma involves the implicit function theorem in higher dimensions (or its close
cousin the inverse function theorem). But we will see below that in our special
case, Theorem 1 is sufficient.
We consider the function G(x,y) = F(b +x,c +y), which effectively translates
0 0
our focus to the origin. Just as a solution to F(b,c) = 0 corresponds to a mean
value abscissa, a solution to G(x,y) = 0 also corresponds to a mean value abscissa;
in particular, G(0,0) = 0 corresponds to the given mean value abscissa c on the
0
interval [a ,b ]. Our assumptions on the partial derivatives of F at (b ,c ) similarly
0 0 0 0
translate G (0,0) = G (0,0) = 0 while G (0,0) = 0 and G (0,0) = 0. A quick
x y xx yy
6 6
calculation shows that G (0,0) = 0 — indeed G (x,y) is always zero! Thus (21)
xy xy
is satisfied, and, if f is four-time continuously differentiable so that G is three-times
continuously differentiable, we can apply the Morse lemma.
In fact, our situation is a bit simpler than the one covered by the Morse lemma,
and so we will only prove the special case of the lemma that we need. What’s

12 DAVID LOWRY-DUDA AND MILES WHEELER
special is that G naturally splits into a function depending only on x and a function
depending only on y: We can write G(x,y) = g (x) g (y), where
1 2
−
f(b + x) f(a )
0 0 ′ ′ ′
(23) g (x) = − f (c ), g (y) = f (c + y) f (c ).
1 0 2 0 0
(b + x) a − −
0 0
−
′
Thus G(x,y) = 0 is equivalent to g (x) = g (y). We include the f (c ) terms in
1 2 0
(23) so that g (0) = g (0) = 0, so we can continue to focus our attention on the
1 2
′ ′
origin. Our assumptions G (0,0) = G (0,0) now translate into g (0) = g (0),
x y 1 2
′
while our assumptions G (0,0) = 0 and G (0,0) = 0 translate into g (0) = 0 and
xx xy 1
′ 6 6 6
g (0) = 0.
2
6
Taylor expanding g and g gives the approximations
1 2
′′ ′′ ′′ ′′′
g (0) 1 f (b ) g (0) f (c )
g (x) 1 x2 = 0 x2, g (y) 2 y2 = 0 y2,
1 2
≈ 2! b a 2! ≈ 2! 2!
0 0
−
and hence the approximation G(x,y) αx2 + βy2 with α = g′′ (0)/2 and β =
1
′′ ≈
g (0)/2. We will show that we can choose coordinates u and v to make this ap-
2
proximation exact while at the same time taking the constants to be 1.
±
To do this, we use Taylor’s theorem to write g and g exactly as
1 2
g (x) = αx2 + r (x)x2 = x2 α + r (x)
1 1 1
g (y) = βy2 + r (y)y2 = y2 (cid:0) β + r (y) (cid:1) ,
2 2 2
(cid:0) (cid:1)
where r (x) and r (y) are remainder terms. Thus r (x) is small when x is near 0
1 2 1
and r (y) is small when y is near 0. Ideally, we would like to take coordinates like
2
u = x α + r (x) and v = y β + r (y), so that G(x,y) = u2 v2 (whose zeros are
1 2
−
very epasy to study). But if,pfor instance, α < 0 and r (x) 0, then we would be
1
≈
trying to take the square root of a negative number!
To get around this, we multiply g (x) by σ = sgn(α), which is 1 if α > 0 and 1
1 1
−
if α < 0. Then σ g (x) = x2(σ α + σ r (x)). As r (x) is the remainder term, we
1 1 1 1 1 1
can choose δ > 0 such that r (x) < α for all x satisfying x < δ. In this interval,
1
| | | | | |
σ α + σ r (x) is always positive. Similarly we multiply g (x) by σ = sgn(β), so
1 1 1 2 2
that σ β > 0. As with r , in a sufficiently small neighborhood around 0 we have
2 1
that r (y) < β , and in this neighborhood σ β + σ r (y) is always positive.
2 2 2 2
| | | |
This allows us to write u = x σ (α + r (x)) and v = y σ (β + r (y)), which
1 1 2 2
is nearly the ideal choices describped above. But to be properpcoordinates we require
these maps to be invertible. To study these potential coordinates, we again use the
implicit function theorem 1. Namely, we study the zeroes of the two functions
(24) F (x,u) = x σ (α + r (x)) u, F (y,v) = y σ (β + r (y)) v
1 1 1 2 2 2
− −
p p
in small neighborhoods of the origin (small enough so that the arguments of the
square roots are always positive). We calculate that F (0,0) = F (0,0) = 0 while
1 2
∂F ∂F ∂F ∂F
1 2 1 2
(0,0) = √σ α, (0,0) = σ β, (0,0) = 1, (0,0) = 1,
1 2
∂x ∂y ∂u − ∂v −
p
all of which are nonzero. By the implicit function theorem, the first two equalities
show that x = X(u) and y = Y (v) in a neighborhood of (x,y,u,v) = (0,0,0,0).
The second two equalities confirm that u = U(x) and v = V (y) also holds in a
neighborhood of the origin. Further, each of these coordinate maps is continuously
differentiable. Thus (x,y) (u,v) is valid change of coordinates.
7→

WHEN ARE THERE CONTINUOUS CHOICES FOR THE MEAN VALUE ABSCISSA? 13
We have proved that G(x,y) = g (x) g (y) = σ u2 σ v2 around a neigh-
1 2 1 2
− −
borhood of the origin, i.e. that the conclusion (22) of the Morse lemma holds. To
continue our investigation of mean value abscissae, we examine
G(x,y) = σ u2 σ v2 = 0.
1 2
−
There are a few different possibilities depending on the combinations of the signs
′′
σ and σ . In terms of the original function f, we note that σ is the sign of f (b )
1 2 1 0
′′′
and σ is the sign of f (c ).
2 0
(i) If σ and σ have opposite signs, then G(x,y) = 0 is equivalent to u2 = v2.
1 2
−
The only solution is (u,v) = (0,0) and this solution is isolated.
(ii) If σ and σ have the same sign, G(x,y) = 0 is equivalent to u2 = v2. This
1 2
has two solutions u = v, and no other nearby solutions.
±
Looking again at Figure 4, we see that case (i) corresponds to the right graph, and
case (ii) corresponds to the left graph.
We summarize the results of our exploration in the following theorem.
Theorem 6. Let f be a four-times continuously differentiable function and fix an
R
interval [a ,b ] . Suppose c is a mean value abscissa for f on the interval
0 0 0
⊂ ′′ ′ ′
[a ,b ], and suppose that f (c ) = 0 and f (b ) = f (c ). Finally, suppose that both
0 0 0 0 0
′′ ′′′
f (b ) and f (c ) are nonzero. Then
0 0
′′ ′′′
If f (b ) and f (c ) have opposite signs, then c cannot be extended to a
0 0 0
•
continuous function c = C(b) near b .
0
′′ ′′′
If f (b ) and f (c ) have the same sign, then there are two continuously
0 0
•
differentiable functions c = C (b) and c = C (b) solving (1) for b near b .
1 2 0
There are no other nearby solutions.
5. Analytic Functions.
′′ ′′
Looking back, if f (c ) = 0 we can use Theorem 4, while if f (c ) = 0 but
0 0
′′′ ′′ 6 ′′
f (c ) = 0 and f (b ) = 0, then we can use Theorem 6. What if f (c ) =
0 0 0
6 6
f′′′ (c ) = 0 but f(4)(c ) = f′′′′ (c ) = 0? Or, even more ambitiously, what if
0 0 0
6
(25) f′ (c ) = f′′ (c ) = = f(k)(c ) = 0 but f(k+1)(c ) = 0
0 0 0 0
··· 6
for k = 10 or k = 200? Ideally we do not want to have to prove a new theorem
for each of these cases. There is also the possibility that all of the derivatives of
f vanish at c . For instance this is what happens at c = 1 for the classic “bump
0 0
function”, defined to be exp( 1/(1 x2)) for 1 < x < 1 and 0 otherwise.
− − −
We can rule out this last possibility by restricting to analytic functions. Recall
that a function f is analytic if the Taylor series for f centered at each point x
0
converges to f in a neighborhood of x . That is, for each x , we have the equality
0 0
∞
f(n)(x )
f(x) = 0 (x x )n
0
n! −
X
n=0
for all x in a neighborhood of x . One of the nice things about analytic functions
0
is that we can only have f(k)(x ) = 0 for all k 1 if f is a constant function. For
0
≥
the rest of this section we will assume that f is a non-constant analytic function,
in which case we can always find a k so that (25) holds.
With this assumption in mind, let us return to the function G(x,y) = F(x +
b ,y + c ), where F is the implicit function (20) whose zeros represent solutions
0 0
to the mean value theorem relation (1). As in the previous section, we will write

14 DAVID LOWRY-DUDA AND MILES WHEELER
G(x,y) = g (x) g (y) where g and g are as in (23). The given mean value
1 2 1 2
−
abscissa implies that g (0) = g (0) = 0. But unlike before, the first nonzero term
1 2
in the Taylor expansion of g is when f(k+1)(c ) = 0, yielding the approximation
2 0
6
g (y) β yk.
2 0
≈
where β = f(k+1)(c )/k! is a nonzero constant. Similarly picking ℓ so that
0 0
(26) f′ (b ) = f′′ (b ) = = f(ℓ−1)(b ) = 0 but f(ℓ)(b ) = 0,
0 0 0 0
··· 6
a slightly more involved calculation shows that
g (x) α xℓ,
1 0
≈
where this time the nonzero constant is α = f(ℓ)(b )/(ℓ!(b a)). We call ℓ and
0 0
−
k the order of vanishing at the origin for g and g , respectively. Our equation
1 2
G(x,y) = 0 now seems to be approximately
α xℓ β yk.
0 0
≈
As in our proof of a special case of the Morse lemma, we will make this precise
by finding new coordinates u,v so that G(x,y) = 0 is exactly either vk = uℓ or
vk = uℓ.
−
As f is analytic, we can see that both g and g are analytic. Representing g
1 2 1
and g by their Taylor expansion near 0, we can write them as
2
∞ ∞
g (x) = xℓ α xm, g (y) = yk β ym,
1 m 2 m
X X
m=0 m=0
where α = 0 and β = 0 were defined above. As with our special case of the Morse
0 0
6 6
lemma, we now multiply g by σ = sgnα and g by σ = sgnβ , enabling us to
1 1 0 2 2 2
take roots in a neighborhood of 0.
Taking these roots, we can define two smooth (in fact analytic) functions by
∞ ∞
1/ℓ 1/k
F (x,u) = x σ α xm u, F (y,u) = y σ β ym v,
1 1 m 2 2 m
− −
(cid:16) X (cid:17) (cid:16) X (cid:17)
m=0 m=0
in a neighborhood of the origin. Suppose for the moment that the equations
F (x,u) = 0 and F (y,v) = 0 defined a smooth change of coordinates (x,y)
1 2
7→
(u,v). Then, in the (u,v) coordinates, we would have g = σ uk and g = σ uℓ so
1 1 2 2
that G(x,y) = 0 was equivalent to
σ
(27) uk = 2 vℓ = vℓ,
σ ±
1
analogous to the Morse lemma but with higher powers.
Checking that F (x,u) = 0 and F (y,v) = 0 define an invertible change of
1 2
coordinates x = X(u) and y = Y (v) can be proved from the implicit function
theorem Theorem 1, and in this case the proof is almost identical to the proof
for (24), the change of coordinates from our consideration of Morse’s lemma. Thus
(x,y) (u,v) is a valid change of coordinates, and we can study G(x,y) = 0 by
7→
studying solutions to (27).
Thinking about the graph of (27) for different values of k and ℓ, and different
combinations of signs of σ and σ , we find that
1 2
(i) If k is odd, then there is one continuous solution v = V (u) of (27) in a
1
neighborhood of the origin, and no other nearby solutions.

WHEN ARE THERE CONTINUOUS CHOICES FOR THE MEAN VALUE ABSCISSA? 15
(ii) If k and ℓ are both even and σ /σ = +1 then there are two continuous
2 1
solutions v = V (u) and v = V (u) of (27) in a neighborhood of the origin,
1 2
and no other nearby solutions.
(iii) If k and ℓ are both even and σ /σ = 1, then the origin is an isolated
2 1
−
solution of (27).
(iv) If k is even and ℓ is odd, then there are two continuous solutions v =
V (u) and v = V (u) of (27), but they are only defined in a one-sided
1 2
neighborhood of the origin where (σ /σ )u 0.
2 1
≥
Since we can always write y = Y (v) and u = U(x), continuously solving for v in
terms of u is equivalent to continuously solving for y in terms of x. As we’re solving
G(x,y) = F(x + b ,y + c ) = 0, this is equivalent to continuously solving (1) for
0 0
the abscissa c = c +y in terms of the endpoint b = b +x for x in a neighborhood
0 0
of (b,c) = (b ,c ).
0 0
Thus we can find a continuous choice of mean value abscissa near any point
where (i) or (ii) hold. The following lemma tells us that there there is always at
least one such point (i) holds.
Lemma 7. Let f be a non-constant analytic function satisfying f(a ) = f(b ) = 0.
0 0
′
Then there is a mean value abscissa c of f on [a ,b ] such that f (c ) = 0 and
0 0 0 0
such that the smallest k 1 such that f(k)(c ) = 0 is even, i.e. such that the order
0
′ ≥ 6
of vanishing of f at c is odd.
0
Proof. Since f is non-constant, f takes an absolute maximum or an absolute min-
imum at a point c within the interval (a ,b ). Notice that c is not an endpoint of
0 0
the interval since f(a ) = f(b ) = 0 and the function is not constant. We choose
0 0
c to be this point c.
0
′
As c is an extremum, f (c ) = 0. From its Taylor expansion, we see that near
0 0
c , f is very closely approximated by f(c ) + a (x c)k, where a = f(k)(c )/(k!).
0 0 k k 0
−
If k were odd, then f would be strictly increasing or decreasing at c , contradicting
0
(cid:3)
the fact that it has a local extremum there.
With this lemma, we are now ready to complete our study of when there exist
continuous choices of mean value abscissae c = C(b). Recall that we assume without
loss of generality that f(a ) = f(b ) = 0. Let c be a mean value abscissa for f
0 0 0
′
on [a ,b ] such that the order of vanishing of f at c is odd, as guaranteed by the
0 0 0
′
lemma. The order of vanishing of f at c is the same as the order of vanishing of
0
g at 0 by construction, and thus the lemma indicates that the k appearing in (27)
2
is odd. Thus we are in case (i), and we can uniquely solve (1) for c = C(b) in a
neighborhood of b . This completes the proof of the following theorem.
0
Theorem 8. Let f be real analytic on the interval [a ,b ]. Then there exists at
0 0
least one mean value abscissa c (a ,b ) such that c is a mean value abscissa for
0 0 0 0
∈
f on [a ,b ], and for which there exists a continuous function c = C(b) such that
0 0
f(b) f(a)
′
− = f (C(b))
b a
−
for all b in a neighborhood of b . There are no other solutions near (b ,c ).
0 0 0
Remark. As a final note, we note that being “merely” infinitely differentiable is
not strong enough to guarantee that there is always a choice of a mean value abscissa
with a continuous dependence on the right endpoint. For a counterexample, see

16 DAVID LOWRY-DUDA AND MILES WHEELER
1
3
f 0 c 2
1
−
1
a b
0 0
0
0 1 2 3 0 1 2 3
x b
Figure 5. A smooth function where no continuous choice of mean
value abscissa exists.
Figure 5. One can construct a smooth function of this shape from bump functions.
On the indicated interval [0,3], every value c with 1 c 2 is a valid mean
0 0
≤ ≤
value abscissa; this is reflected in the mean value abscissa plot on the right by a
vertical line segment from (3,1) to (3,2). For b just to the left of b , the slope of
0
the secant line is negative, and for b just to the right of b , the slope of the secant
0
line is positive. But any value c is either at least distance 1/2 away from a point
0
′ ′
c where f (c) < 0 or a point c where f (c) > 0. There is no continuous choice of
mean value abscissa for this function.
6. Reflection and Further Questions.
The major selling-point of Theorem 8 is that it gives us a continuous choice c =
C(b) of mean value abscissa without any assumptions on f other than analyticity.
On the other hand, in cases where we do know more about our favorite abscissa
c , the classification (i)–(iv) of the curves (27) gives much more information about
0
nearby solutions. And for the local picture, we should expect “most” points for
“most” intervals to not be degenerate enough that Theorem 4 and Theorem 6 both
fail.
There are many more questions that one could ask about the set of solutions
to (1). Firstly, what if you allow the left endpoint a to vary as well as b and look
for continuous choices c = C(a,b)? The techniques we have used will still be very
powerful, but for instance the decomposition G(x,y) = g (x) g (y) in the above
1 2
−
section will no longer be as simple.
One could also study the global structure of the solution sets shown in Figures 3
and 4. How many different connected components are there? In what ways can they
“begin” and “end”? Answering such questions will require very different techniques.
Acknowledgements
D Lowry-Duda was supported by the National Science Foundation Graduate
Research Fellowship Program under Grant No. DGE 0228243 and the EPSRC Pro-
gramme Grant EP/K034383/1 LMF: L-Functions and Modular Forms.

|    |    |    |    |
|:---|:---|:---|:---|
|    |    |    |    |
|    |    |    |    |
|    |    |    |    |

WHEN ARE THERE CONTINUOUS CHOICES FOR THE MEAN VALUE ABSCISSA? 17
Miles H. Wheeler was supported by the National Science Foundation under Grant
No. DMS-1400926.
We also thank the many contributors to the python programming packages
NumPy, SymPy, and matplotlib, as we used this software for our own exploration
and to create the functions and figures in this article. A copy and description of
the code used for this article are available at
http://davidlowryduda.com/choosing-functions-for-mvt-abscissa/.
References
[1] Carter, P. Lowry-Duda, D. (2017) On functions whose mean value abscissas are midpoints,
with connections to harmonic functions. Amer. Math. Monthly, 124(6), 535–542.
[2] Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in science & engi-
neering, 9(3), 90.
[3] Matsumoto, Y. (2002). An introduction to Morse theory. Iwanami series in mathematics (Vol.
208). Providence, RI: American Mathematical Society.
[4] Meurer, A., Smith, C. P., Paprocki, M., ertk, O., Kirpichev, S. B., Rocklin, M., A., Ivanov, S.,
Moore, J.K., Singh, S. and Rathnayake, T. (2017). SymPy: symbolic computing in Python.
PeerJ Computer Science, 3, e103.
[5] Oliphant, T. E. (2006). A guide to NumPy (Vol. 1, p. 85). USA: Trelgol Publishing.
[6] Strichartz, R. S. (2000). The way of analysis. Sudbury, MA: Jones & Bartlett Learning.