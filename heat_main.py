from __future__ import print_function
import time
import argparse

import heat
import cy_heat


def main(input_file, a=0.5, dx=0.1, dy=0.1, timesteps=200, image_interval=4000):

    compilers = {'heat' : heat, 'cy_heat' : cy_heat}

    for compiler in compilers :
        # Initialise the temperature field
        field, field0 = compilers[compiler].init_fields(input_file)

        print("Heat equation solver")
        print("Diffusion constant: {}".format(a))
        print("Input file: {}".format(input_file))
        print("Language: {}".format(compiler))
        print("Parameters")
        print("----------")
        print("  nx={} ny={} dx={} dy={}".format(field.shape[0], field.shape[1], dx, dy))
        print("  time steps={}  image interval={}".format(timesteps, image_interval))

        # Plot/save initial field
        compilers[compiler].write_field(field, 0, compiler, input_file[:-4])
        # Iterate
        t0 = time.time()
        compilers[compiler].iterate(field, field0, a, dx, dy, timesteps, image_interval)
        t1 = time.time()
        # Plot/save final field
        compilers[compiler].write_field(field, timesteps, compiler, input_file[:-4])

        print("Simulation finished in {0} s\n".format(t1-t0))

if __name__ == '__main__':

    bottles = ['bottle.dat','bottle_medium.dat','bottle_large.dat']

    for bottle in bottles :
        # Process command line arguments
        parser = argparse.ArgumentParser(description='Heat equation')
        parser.add_argument('-dx', type=float, default=0.01,
                            help='grid spacing in x-direction')
        parser.add_argument('-dy', type=float, default=0.01,
                            help='grid spacing in y-direction')
        parser.add_argument('-a', type=float, default=0.5,
                            help='diffusion constant')
        parser.add_argument('-n', type=int, default=200,
                            help='number of time steps')
        parser.add_argument('-i', type=int, default=4000,
                            help='image interval')
        parser.add_argument('-f', type=str, default=bottle, 
                            help='input file')

        args = parser.parse_args()

        main(args.f, args.a, args.dx, args.dy, args.n, args.i)

