from flask import Flask
from flask_restplus import Resource, Api, fields

import process

app = Flask(__name__, static_url_path='/static')
api = Api(app, version='1.0', title='FlaskLocal', description='FlaskLocal')

ns_spark = api.namespace('spark', description='spark API')
spark_response = ns_spark.model("test_response",{
    "unknown_person": fields.Boolean,
    "fire_broken" : fields.Boolean
})

spark_request = ns_spark.model('test_request', {
    'data': fields.String
})

#앱빌더를 통해 새 게시물 & 댓글 알림 수신
@ns_spark.route('/process')
class test(Resource):
    @ns_spark.doc('post')
    @ns_spark.expect(spark_request)
    #@ns_spark.marshal_with(spark_response)
    def post(self):
        #print(api.payload)
        res = spark.ProcessImage(api.payload)
        return res
        #검증용 line
        #return {'challenge':api.payload['challenge']}

if __name__ == '__main__':
    spark = process. Process()
    app.run(host='0.0.0.0', port=80, threaded=False)