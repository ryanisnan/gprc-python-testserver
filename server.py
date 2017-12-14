# Library imports
from concurrent import futures
import grpc

# Local imports
from matches_pb2 import CareerMatch
from matches_pb2 import CareerMatchesResponse
from matches_pb2_grpc import CareerMatchesServiceStub
from matches_pb2_grpc import add_CareerMatchesServiceServicer_to_server


class CareerMatchesServicer(CareerMatchesServiceStub):
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
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_CareerMatchesServiceServicer_to_server(CareerMatchesServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()


if __name__ == '__main__':
    serve()
