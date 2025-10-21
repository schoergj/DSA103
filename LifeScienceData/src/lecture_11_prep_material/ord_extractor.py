# import requirements
from ord_schema.message_helpers import load_message, write_message
from ord_schema.proto import dataset_pb2

# load the binary ord file
dataset = load_message(r"C:\Users\jschoer\Desktop\DSA103 Coding and Tests\ord-data\data\5e\ord_dataset-5e8318f0dda04b398c14f4c3adfeb32c.pb.gz", dataset_pb2.Dataset)
# save the ord file as human readable text
write_message(dataset, "ORD_Aza_Heck_Dataset.pbtxt")