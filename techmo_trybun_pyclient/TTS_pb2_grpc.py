# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import TTS_pb2 as TTS__pb2


class TTSStub(object):
  """Techmo TTS Service API
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Synthesize = channel.unary_stream(
        '/herold.TTS/Synthesize',
        request_serializer=TTS__pb2.SynthesizeRequest.SerializeToString,
        response_deserializer=TTS__pb2.SynthesizeResponse.FromString,
        )


class TTSServicer(object):
  """Techmo TTS Service API
  """

  def Synthesize(self, request, context):
    """Return speech using given text and optional configuration
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TTSServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Synthesize': grpc.unary_stream_rpc_method_handler(
          servicer.Synthesize,
          request_deserializer=TTS__pb2.SynthesizeRequest.FromString,
          response_serializer=TTS__pb2.SynthesizeResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'herold.TTS', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
