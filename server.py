# Library imports
from concurrent import futures
import grpc
import logging
import time

# Local imports
from matches_pb2 import CareerMatch
from matches_pb2 import CareerMatchesResponse
import matches_pb2_grpc


# Logging config
logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)


class CareerMatchesServiceServicer(matches_pb2_grpc.CareerMatchesServiceServicer):
    """
    Implementation of the service in python.
    """
    def GetMatches(self, request, context):
        matches = [
            CareerMatch(career_id=1, score=5.0),
            CareerMatch(career_id=2, score=4.5),
            CareerMatch(career_id=3, score=2.0),
            CareerMatch(career_id=4, score=1.0),
        ]
        return CareerMatchesResponse(matches=matches)


def serve():
    logger.info('serve() running')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    matches_pb2_grpc.add_CareerMatchesServiceServicer_to_server(CareerMatchesServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    # Hang while we serve
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        logger.info('serve() interrupted by keyboard input')
        server.stop(0)


if __name__ == '__main__':
    serve()
