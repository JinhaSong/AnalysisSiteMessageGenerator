from AnalysisSiteRequestGenerator import AnalysisSiteRequestGenerator
from utils import *
import argparse

def parse_arguments():
    """Parse input arguments"""
    parser = argparse.ArgumentParser(description='sogang-mm analysis-site requests generator')
    parser.add_argument("--url", dest='url', help='URL of analysis-site', type=str)
    parser.add_argument("--image_path", dest='image_path', help='Image path to send as request', type=str)
    parser.add_argument("--modules", dest='modules', help='names of analysis-module', type=str)
    parser.add_argument("--num_of_messages", dest='num_of_messages', help="number of request messages to send", type=int)

    return parser

if __name__ == '__main__':
    try :
        args = parse_arguments().parse_args()

        request_generator = AnalysisSiteRequestGenerator()

        num_of_messages = args.num_of_messages

        for i in range(0, num_of_messages) :
            b_image = load_binary_image(args.image_path)
            request_generator.set_request_attr(url=args.url, image=b_image, modules=args.modules)
            response = request_generator.send_request_message()

    except :
        parse_arguments().print_help()