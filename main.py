from AnalysisSiteRequestGenerator import AnalysisSiteRequestGenerator
from utils import *
import argparse

def parse_args():
    """Parse input arguments"""
    parser = argparse.ArgumentParser(description='sogang-mm analysis-site requests generator')
    parser.add_argument("--url", dest='url', help='URL of analysis-site', type=str)
    parser.add_argument("--image_path", dest='image_path', help='Image path to send to request', type=str)
    parser.add_argument("--modules", dest='modules', help='names of analysis-module', type=str)
    parser.add_argument("--numofmessages", dest='num_of_messages', help="number of request", type=int)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    pass