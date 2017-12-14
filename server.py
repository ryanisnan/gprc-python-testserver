# Library imports
from concurrent import futures
import grpc

# Local imports
from matches_pb2 import CareerMatch
from matches_pb2 import CareerMatchesResponse
import matches_pb2_grpc


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
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    matches_pb2_grpc.add_CareerMatchesServiceServicer_to_server(CareerMatchesServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()


if __name__ == '__main__':
    serve()
