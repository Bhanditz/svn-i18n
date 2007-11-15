import logging
import optparse

def make_option_parser():
    """Return an optparse.OptionParser configured for the make_cc_files 
    command line script."""

    parser = optparse.OptionParser()
    parser.set_defaults(verbosity=logging.WARNING)

    # settings
    parser.add_option('-m', '--master', dest='english_po',
                      default='master/cc_org.po',
                      help='Master .po file, used to map keys.')
    parser.add_option('-q', '--quiet', dest='verbosity',
                      action='store_const', const=logging.ERROR)
    parser.add_option('-v', dest='verbosity', 
                      action='store_const', const=logging.INFO)
    parser.add_option('--noisy', dest='verbosity', 
                      action='store_const', const=logging.DEBUG)

    # input options
    parser.add_option('-i', '--input-dir', dest='input_dir',
                      help='Directory to search for .po files to convert.')

    # output options
    parser.add_option('-o', '--output-dir', dest='output_dir', 
                      help='Output directory for CC-style .po files.')

    return parser

def parse_args(**defaults):
    """Parse the optoins and arguments from the command-line and make sure
    required values are present.  [defaults] is a dict containing the default
    values to pass to the parser.

    Returns a two tuple: (options, args).
    """

    parser = make_option_parser()
    parser.set_defaults(**defaults)


    options, args = parser.parse_args()

    # make sure an input and output directory were specified
    if not(options.input_dir):
        parser.error("An input directory must be supplied.")
    
    if not(options.output_dir):
        parser.error("An output directory must be supplied.")


    return options, args
