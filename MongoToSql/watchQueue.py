# coding=utf-8
#!/usr/local/bin/python3
import boto3
from mongo_mysql_actions import getReservation
import os

client = boto3.client('sqs', region_name='eu-west-1')
# client.create_queue(QueueName='queueVdm')
queues = client.list_queues(QueueNamePrefix=os.environ['QUEUE_NAME_PREFIX'])
test_queue_url = queues['QueueUrls'][0]

exit = True
exit_command = "exit"

while True:
    messages = client.receive_message(QueueUrl=test_queue_url,MaxNumberOfMessages=10) # adjust MaxNumberOfMessages if needed
    if 'Messages' in messages: # when the queue is exhausted, the response dict contains no 'Messages' key
        for message in messages['Messages']: # 'Messages' is a list
            # process the messages
	    document_id = message['Body']
            print(document_id)
       	    receipt_handle = message['ReceiptHandle']
	    # Change visibility timeout of message from queue
	    client.change_message_visibility(
		QueueUrl=test_queue_url,
    		ReceiptHandle=receipt_handle,
    		VisibilityTimeout=20
	    )
	    print('Received and changed visibility timeout of message: %s' % message)
	    reservation_OK = getReservation(document_id)
            # next, we delete the message from the queue so no one else will process it again
            if reservation_OK == True:
		client.delete_message(QueueUrl=test_queue_url,ReceiptHandle=message['ReceiptHandle'])
print("Bye")


# ##################### DEAMON FOR SQS LISTEN MESSAGE but not working :( #######################

#from sqs_listener import SqsListener


#class MyListener(SqsListener):
#    def handle_message(self, body, attributes, messages_attributes):
#        print(body)
#	print("hello")
        #run_my_function(body['param1'], body['param2'])

#listener = MyListener('queueVdm',  region_name='eu-west-1')
#listener.listen()
