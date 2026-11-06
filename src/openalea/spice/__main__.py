import argparse

from openalea.spice.configuration import Configuration
from openalea.spice.simulator import Simulator


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="",
        help="The configuration file for the simulation.",
    )
    parser.add_argument(
        "-p",
        "--nb_photons",
        type=int,
        default=100000,
        help="The number of photons to simulate.",
    )
    parser.add_argument(
        "-d",
        "--max_depth",
        type=int,
        default=1,
        help="The maximum number of bounces of each photon.",
    )
    parser.add_argument(
        "-t",
        "--nb_thread",
        type=int,
        default=4,
        help="The number of threads to compute with.",
    )
    parser.add_argument(
        "-b",
        "--backface_culling",
        type=bool,
        default=True,
        help="Whether or not to use backface culling.",
    )
    parser.add_argument(
        "-r",
        "--rendering",
        type=bool,
        default=True,
        help="Whether or not to render images.",
    )
    parser.add_argument(
        "-k",
        "--keep-all",
        type=bool,
        default=True,
        help="Whether or not to keep all photons between steps (very memory intensive).",
    )
    parser.add_argument(
        "-o",
        "--optical_properties",
        type=str,
        default="",
        help="The directory containing the optical properties.",
    )
    parser.add_argument(
        "-s",
        "--scale",
        type=float,
        default=1.0,
        help="The size of geometries. The vertices of geometries is"
             " recalculated by dividing their coordinates by this value",
    )
    parser.add_argument(
        "-bs",
        "--base_spectral_range",
        type=int,
        default=(400, 800),
        help="The base spectral range which includes all the other spectral ranges. "
             "The first value is the start of band and the second is the end of band. Ex: 100 200.",
    )
    parser.add_argument(
        "-e",
        "--environment_file",
        type=str,
        default="",
        help="The file of the 3d environment.",
    )
    args = parser.parse_args()
    configuration = Configuration(nb_photons=args.nb_photons, max_depth=args.max_depth, nb_thread=args.nb_thread,
                                  backface_culling=args.backface_culling, rendering=args.rendering,
                                  keep_all=args.keep_all, optical_properties_dir=args.optical_properties,
                                  environment_file=args.environment_file, base_spectral_range=args.base_spectral_range,
                                  scale_factor=args.scale)
    sim = Simulator(config_file=args.config, configuration=configuration)

    sim.run()


if __name__ == "__main__":
    main()
