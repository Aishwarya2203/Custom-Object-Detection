Python 3.6 required
Tensorflow 1.0 required
OpenCV2 required
Protobuf required

*****************************************************************************************************************************
Running the files
*****************************************************************************************************************************
Go to main/object-detection

Run the object_detection.py file
******************************************************************************************************************************
Custom Training
******************************************************************************************************************************
Use ImageLable for drawing bounding boxes and save in XML format
Convert Xml Images to csv files using xml to csv
Convert csv to tf.record using tf.record file
run the train.py file
export the inference graph
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix training/model.ckpt-180 --output_directory aishwarya
\set TF_CPP_MIN_LOG_LEVEL=2
******************************************************************************************************************************
Results
********************************************************************************************************************************
