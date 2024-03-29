# TsinghuaCFD
This project is created to store my homework codes of the Tsinghua CFD lecture. 

## Homework 22 March

### Question

试用某种差分格式求解二维热传导方程

$$
\frac{\partial u}{\partial t}=\gamma\left(\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}\right) \quad(\gamma>0)
$$

求解域、边界条件及初始条件自定。请给出所用的差分格式、程序和计算结果（如何用图表示？）。此外，如何验证你的计算结果是正确的

### Solution

HW22March.py

## Homework 24 April

### Question

上机实习。线性波动方程$\frac{\partial u}{\partial x}+a \frac{\partial u}{\partial x}=0, a=1$。求解域为：$(x, t) \in[-0.5,0.5] \times[0, \infty]$。初值条件为：
$$
f(x)= \begin{cases}0 & -0.5 \leq x<-0.25 \\ 1 & -0.25 \leq x \leq 0.25 \\ 0 . & 0.25<x \leq 0.5\end{cases}
$$

边界上满足周期条件。取计算网格点为$M_x=100$。$CFL=0.5$。用一阶迎风格式、Lax－Wendroff格式、Warming－Beam格式计算$t=0.1,1.0,10.0$时的数值解。分析数值解在间断附近的行为。

### Solution

HW29March.py