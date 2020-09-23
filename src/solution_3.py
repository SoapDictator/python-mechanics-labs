import sympy as sym
import matplotlib.style as mplstl
import sympy.plotting as symplot

mplstl.use('seaborn-whitegrid')

t = sym.Symbol('t')

A = 0.01
k = 0.4
m0 = 0.1


# 1
# omega0 = sym.sqrt(k / m0)
# x = A * sym.cos(t * omega0)

# x_plot = sym.plot(x, (t, 0, 6), show=False)
# x_plot.title = 'Зависимость координаты материальной точки x от времени t'
# x_plot.xlabel = 't, с'
# x_plot.ylabel = 'x, м'
# x_plot.show()

# v = x.diff(t)

# v_plot = sym.plot(v, (t, 0, 6), show=False)
# v_plot.title = 'Зависимость скорости материальной точки v от времени t'
# v_plot.xlabel = 't, с'
# v_plot.ylabel = 'v, м/с'
# v_plot.show()

# a = v.diff(t)

# a_plot = sym.plot(a, (t, 0, 6), show=False)
# a_plot.title = 'Зависимость ускорения материальной точки a от времени t'
# a_plot.xlabel = 't, с'
# a_plot.ylabel = 'a, м/с^2'
# a_plot.show()


# 2
m = sym.Symbol('m')

omega = sym.sqrt(k / m)
omega_func = sym.lambdify(m, omega)

x1 = sym.cos(t * omega_func(m0))
x1_plot = sym.plot(
    x1, (t, 0, 6),
    label='m0',
    line_color='b',
    legend=True,
    show=False)
x1_plot.title = 'Зависимость координаты материальной точки x от времени t'
x1_plot.xlabel = 't, с'
x1_plot.ylabel = 'x, м'

x2 = sym.cos(t * omega_func(m0 * 2))
x2_plot = sym.plot(
    x2, (t, 0, 6),
    label='2*m0',
    line_color='r',
    legend=True,
    show=False)
x1_plot.extend(x2_plot)

x3 = sym.cos(t * omega_func(m0 * 3))
x3_plot = sym.plot(
    x3, (t, 0, 6),
    label='3*m0',
    line_color='g',
    legend=True,
    show=False)
x1_plot.extend(x3_plot)

x1_plot.show()

x = sym.cos(t * omega)
x_plot3d = symplot.plot3d(
    x, (t, 0, 6), (m, m0, 3 * m0), show=False)
x_plot3d.title = ('Зависимость координаты материальной точки x '
    'от времени t и массы m')
x_plot3d.xlabel = 't, с'
x_plot3d.ylabel = 'm, кг'

x_plot3d.show()
