import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')

t = sym.Symbol('t')

A = 0.01
k = 0.4
m0 = 0.1


# 1
omega0 = sym.sqrt(k / m0)
x = A * sym.cos(t * omega0)

x_plot = sym.plot(x, (t, 0, 6), show=False)
x_plot.title = 'Зависимость координаты материальной точки x от времени t'
x_plot.xlabel = 't, с'
x_plot.ylabel = 'x, м'
# x_plot.show()

v = x.diff(t)

v_plot = sym.plot(v, (t, 0, 6), show=False)
v_plot.title = 'Зависимость скорости материальной точки v от времени t'
v_plot.xlabel = 't, с'
v_plot.ylabel = 'v, м/с'
# v_plot.show()

a = v.diff(t)

a_plot = sym.plot(a, (t, 0, 6), show=False)
a_plot.title = 'Зависимость ускорения материальной точки a от времени t'
a_plot.xlabel = 't, с'
a_plot.ylabel = 'a, м/с^2'
# a_plot.show()


# 2
m = sym.Symbol('m')

omega = sym.sqrt(k / m)
omega_func = sym.lambdify(m, omega)

x1_1 = sym.cos(t * omega_func(m0))
x1_1_plot = sym.plot(
    x1_1, (t, 0, 6),
    label='m0',
    line_color='b',
    legend=True,
    show=False)

x1_2 = sym.cos(t * omega_func(m0 * 2))
x1_2_plot = sym.plot(
    x1_2, (t, 0, 6),
    label='2*m0',
    line_color='r',
    legend=True,
    show=False)
x1_1_plot.extend(x1_2_plot)

x1_3 = sym.cos(t * omega_func(m0 * 3))
x1_3_plot = sym.plot(
    x1_3, (t, 0, 6),
    label='3*m0',
    line_color='g',
    legend=True,
    show=False)
x1_1_plot.extend(x1_3_plot)

x1_1_plot.title = 'Зависимость координаты материальной точки x от времени t'
x1_1_plot.xlabel = 't, с'
x1_1_plot.ylabel = 'x, м'
# x1_1_plot.show()

x = sym.cos(t * omega)
x1_plot3d = symplot.plot3d(
    x, (t, 0, 6), (m, m0, 3 * m0), 
	show=False)
x1_plot3d.title = ('Зависимость координаты материальной точки x '
    'от времени t и массы m')
x1_plot3d.xlabel = 't, с'
x1_plot3d.ylabel = 'm, кг'

# x1_plot3d.show()


# 3
r = sym.Symbol('r')
r_val = [0.05, 0.07, 0.10]
delta = []
x2 = []

for i in range(0, len(r_val)):
	delta.append(r_val[i] / (2 * m0))
	
for i in range(0, len(delta)):
	x2.append(A * sym.cos(t * omega0) * sym.exp(-t * delta[i]))
	
x2_1_plot = sym.plot(
	x2[0], (t, 0, 6),
	label='r=0.05',
	line_color='b',
	legend=True,
	show=False)

x2_2_plot = sym.plot(
	x2[1], (t, 0, 6),
	label='r=0.07',
	line_color='r',
	legend=True,
	show=False)
x2_1_plot.extend(x2_2_plot)

x2_3_plot = sym.plot(
	x2[2], (t, 0, 6),
	label='r=0.10',
	line_color='g',
	legend=True,
	show=False)
x2_1_plot.extend(x2_3_plot)
	
x2_1_plot.title = 'Зависимость координаты материальной точки x от времени t'
x2_1_plot.xlabel = 't, с'
x2_1_plot.ylabel = 'x, м'
# x2_1_plot.show()

x2_expr = A * sym.cos(t * omega0) * sym.exp(-t * (r / (2 * m0)))
x2_plot3d = symplot.plot3d(
    x2_expr, (t, 0, 6), (r, r_val[0], r_val[len(r_val)-1]),
	show=False)
x2_plot3d.title = ('Зависимость коорд. мат. точки x '
    'от времени t и коэфф. вязкого трения r')
x2_plot3d.xlabel = 't, с'
x2_plot3d.ylabel = 'r'
# x2_plot3d.show()

# 4
om = sym.Symbol('om')
delta0 = delta[0]
om_val = [1, 2, 3]
A = []
fi = []
x3 = []

for i in range(0, len(om_val)):
	A.append(1 / (sym.sqrt((omega0**2 - om_val[i]**2)**2 + 4 * delta0**2 * om_val[i]**2)))
	fi.append(sym.atan(2 * delta0 * om_val[i] / (omega0**2 - om_val[i]**2)))
	
	x3.append(A[i] * sym.cos(t * om_val[i] + fi[i]))
	
x3_1_plot = sym.plot(
	x3[0], (t, 0, 6),
	label='om=1',
	line_color='b',
	legend=True,
	show=False)

x3_2_plot = sym.plot(
	x3[1], (t, 0, 6),
	label='om=2',
	line_color='r',
	legend=True,
	show=False)
x3_1_plot.extend(x3_2_plot)

x3_3_plot = sym.plot(
	x3[2], (t, 0, 6),
	label='om=3',
	line_color='g',
	legend=True,
	show=False)
x3_1_plot.extend(x3_3_plot)
	
x3_1_plot.title = 'Зависимость координаты материальной точки x от времени t'
x3_1_plot.xlabel = 't, с'
x3_1_plot.ylabel = 'x, м'
# x3_1_plot.show()

A_expr = 1 / (sym.sqrt((omega0**2 - om**2)**2 + 4 * delta0**2 * om**2))
fi_expr = sym.atan(2 * delta0 * om / (omega0**2 - om**2))
x3_expr = A_expr * sym.cos(t * om + fi_expr)

x3_plot3d = symplot.plot3d(
    x3_expr, (t, 0, 6), (om, om_val[0], om_val[len(om_val)-1]),
	show=False)
x3_plot3d.title = ('Зависимость коорд. мат. точки x '
    'от времени t и вынуждающей силы omega')
x3_plot3d.xlabel = 't, с'
x3_plot3d.ylabel = 'omega'
x3_plot3d.show()