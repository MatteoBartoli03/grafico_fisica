import numpy as np
import matplotlib.pyplot as pl

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
S = -3*np.cos(X)

fig = pl.figure(figsize=(8, 4))
ax = pl.subplot(111)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',0))

ax.patch.set_edgecolor('k')
ax.patch.set_linewidth(1)

ax.set_xlim(0, X.max() * 1.1)

ax.xaxis.set_ticks([-np.pi, -np.pi/2 ,0, np.pi/2, np.pi])
ax.xaxis.set_ticklabels([ r'$0$', r'$+0,36$', r'$+0,72$', r'$+1,08$', r'$+1,44$',])

ax.yaxis.set_ticks([-3, 0, +3])
ax.yaxis.set_ticklabels([r'$-0,030$', r'$0$', r'$+0,030$'])


ax.xaxis.set_label_text('$tempo (s)$')
ax.xaxis.set_label_coords( x = 0.5 , y = -0.05)

ax.yaxis.set_label_text('$spazio (m)$')
ax.yaxis.set_label_coords( x = -0.1 , y = 0.5)

#etichette 
ax.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="oscillazione armonica \ndi un pendolo a molla")

#legenda
ax.legend(loc='best')

pl.savefig("./oscillazione.png", dpi=1000)
pl.show()