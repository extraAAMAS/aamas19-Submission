import argparse
import os
import sys
import time

from qlearn import train, test

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description=__doc__)

    argparser.add_argument(
        '--mode',
        default='train',
        type=str
    )
    argparser.add_argument(
        '--env-name',
        default='FourLargeRooms',
        type=str
    )
    argparser.add_argument(
        '--alpha',
        default=0.2,
        type=float
    )
    argparser.add_argument(
        '--epsilon',
        default=0.1,
        type=float
    )
    argparser.add_argument(
        '--discount',
        default=0.99,
        type=float
    )
    argparser.add_argument(
        '--num-iters',
        default=1000,
        type=int
    )
    argparser.add_argument(
        '--num-seeds',
        default=10,
        type=int
    )
    argparser.add_argument(
        '--policy-dir',
        default='saved_qvalues/optimal_qvalues',
        type=str
    )
    argparser.add_argument(
        '-ma', '--match-action',
        action='store_true',
        dest='debug',
        help='Match actions with ground truths and generate plots'
    )
    argparser.add_argument(
        '-v', '--verbose',
        action='store_true',
        dest='debug',
        help='print debug information')

    args = argparser.parse_args()

    start = time.time()
    if args.mode == 'train':
        train.train(args)
    else:
        test.test(args)
    end = time.time()
    print ("Time taken: ", end - start)