from flask import Flask
FAI=Flask(__name__)
@FAI.route('/wish/<na>')
def wish(na):
    return f'Hello, How are you {na}'
if __name__=='__main__':
    FAI.run(debug=True,port=5000,host='192.168.222.220')
