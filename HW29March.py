import numpy as np
import matplotlib.pyplot as plt


##############################
# Functions
##############################
class Arg:
    M, A, C = 100, 1, 0.5
    F_0 = np.array([1 if i/100>=0.25 and i/100<=0.75 else 0 for i in range(101)])
    delta_x, delta_t = 1/100, 0.5/100
    n1, n2, n3 = int(0.1/delta_t), int(1.0/delta_t), int(10.0/delta_t)

def one_order(args:Arg):
    u = np.zeros([args.n3+1, args.M+1])
    u[0] = args.F_0
    for i in range(1, args.n3+1):
        for j in range(1, args.M+1):
            u[i,j] = u[i-1,j] - args.C * ( u[i-1,j] - u[i-1,j-1] )
        u[i,0] = u[i,-1]

    return u

def Lax_Wendroff(args:Arg):
    u = np.zeros([args.n3+1, args.M+1])
    u[0] = args.F_0
    for i in range(1,args.n3+1):
        for j in range(1,args.M):
            u[i,j] = ( 1 - args.C**2 ) * u[i-1,j] + ( args.C - 1 ) * args.C / 2 * u[i-1,j+1] + ( args.C + 1 ) * args.C / 2 * u[i-1,j-1]
        edge = ( 1 - args.C**2 ) * u[i-1,0] + ( args.C - 1 ) * args.C / 2 * u[i-1,1] + ( args.C + 1 ) * args.C / 2 *u[i-1,-2]
        u[i,0] = edge
        u[i,-1] = edge

    return u

def Warming_Beam(args:Arg):
    u = np.zeros([args.n3+1, args.M+1])
    u[0] = args.F_0
    for i in range(1,args.n3+1):
        for j in range(2,args.M+1):
            u[i,j] = ( 1 - 3 * args.C / 2 + args.C**2 / 2 ) * u[i-1,j] + ( 2 - args.C ) * args.C * u[i-1,j-1] \
                + ( args.C - 1 ) * args.C / 2 * u[i-1,j-2]
        u[i,0] = u[i,-1]
        u[i,1] = ( 1 - 3 * args.C  / 2 + args.C**2 / 2 ) * u[i-1,1] + ( 2 - args.C ) * args.C * u[i-1,0]\
            + ( args.C - 1 ) * args.C / 2 * u[i-1,-2]
    
    return u


##############################
# Calculations
##############################
# parameter
args = Arg()
args.M, args.A, args.C = 100, 1, 0.5
args.F_0 = np.array([1 if i/100>=0.25 and i/100<=0.75 else 0 for i in range(101)])
args.delta_x, args.delta_t = 1/100, 0.5/100
args.n1, args.n2, args.n3 = int(0.1/args.delta_t), int(1.0/args.delta_t), int(10.0/args.delta_t)

# calculations
u_one = one_order(args)
u_LW = Lax_Wendroff(args)
u_WB = Warming_Beam(args)

# draw and save figs
def plot_save(u, title, save_path,args:Arg):
    data = [u[args.n1], u[args.n2], u[args.n3]]  
    x = np.arange(args.M+1) / args.M - 0.5 

    fig, ax = plt.subplots()
    ax.plot(x, data[0], label=f"t=0.1")  # 绘制第一个曲线
    ax.plot(x, data[1], label=f"t=1.0")  # 绘制第二个曲线
    ax.plot(x, data[2], label=f"t=10.0")  # 绘制第三个曲线

    ax.set_title(title)
    ax.legend()
    ax.set_xlabel("x")
    ax.set_ylabel("u(t)")
    
    plt.savefig(save_path)

plot_save(u_one, 'one order upwind', 'one_order.png', args)
plot_save(u_LW, 'Lax Wendroff', 'Lax_Wendroff.png', args)
plot_save(u_WB, 'Warming Beam', 'Warming_Beam.png', args)
print('Done')