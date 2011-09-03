#    two dimensional plotting
import pylab as p

#    three dimensional plotting
import mpl_toolkits.mplot3d.axes3d as p3

def visualize(R):
    #    can only plot 2D or 3D
    if R.shape[0] > 3:
        print('can only plot 2D or 3D')
        return
    
    fig = p.figure()
    
    # scatter3D requires a 1D array for x, y, and z
    if R.shape[0] == 3:
        ax = p3.Axes3D(fig)
        ax.scatter3D(R[0, :], R[1, :], R[2, :])

    else:
        #       ax = p.Axes(fig)
        p.scatter(R[0, :], R[1, :])
        
    p.show()
