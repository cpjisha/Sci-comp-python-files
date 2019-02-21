#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:45:19 2019

@author: jisha
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.figure('Snells Law')
plt.plot([10,10],[0,1], 'k', linewidth=2)
plt.xlim([0,20])
plt.ylim([0,1])
plt.axis('off')

plt.arrow(0,0,10,0.5,head_width=0.05,lw=4,length_includes_head=True,head_length=1, fc='r', ec='r')

plt.text(5,0.4,'$\Theta_1$',fontsize=25)
plt.text(11.5,0.55,'$\Theta_2$',fontsize=25)
plt.text(5,0.6,'$\Theta_r$',fontsize=25)
plt.text(5,0.9,'$n_1$',fontsize=25)
plt.text(15,0.9,'$n_2$',fontsize=25)
plt.plot([0,20],[0.5,0.5],'g',linestyle='--')

rectangle =plt.Rectangle((10,0),10,1,linewidth=1,edgecolor='none',facecolor='lavenderblush')
# Add the patch to the Axes
plt.gca().add_patch(rectangle)

rectangle =plt.Rectangle((0,0),10,1,linewidth=1,edgecolor='none',facecolor='mistyrose')
# Add the patch to the Axes
plt.gca().add_patch(rectangle)

plt.arrow(10,0.5,5,0.5,head_width=0.05,lw=4,length_includes_head=True,head_length=1, fc='r', ec='r')
#plt.arrow(10,0.5,1,0.5,head_width=0.1,lw=4,length_includes_head=True,head_length=0.3, fc='r', ec='r')

plt.arrow( 10, 0.5, 0, 0.4, fc="r", ec="r",
head_width=0.5, head_length=0.1,lw=2 )

plt.arrow( 10, 0.5, -10, 0.49,length_includes_head=True, fc="r", ec="r",
head_width=0.05, head_length=1,lw=4 )

#plt.arrow(0,0.5,0,0.5,shape='full',head_width=2,linestyle='--',lw=5,length_includes_head=True,head_length=0.1, fc='r', ec='r')
#plt.arrow(10,0.5,-5,0.5,shape='full',head_width=0.5,linestyle='-',lw=5,length_includes_head=True,head_length=0.3, fc='r', ec='r')
#plt.arrow(10,0.5,10,-0.5,head_width=0.05,lw=4,length_includes_head=True,head_length=1, fc='r', ec='r')

plt.show()

#save the figure
file= ('FigSketchSnell.png')
plt.savefig(file) 
plt.tight_layout()



#plt.figure('arrow')
#plt.arrow( 0, 0.7, 0.0, 0.2, fc="k", ec="k",
#head_width=0.05, head_length=0.1 )