from waitress import serve
import predict

serve(predict.app, host='0.0.0.0', port=8080)
#host='0.0.0.0' สามารถให้คนอื่นเห็นได้