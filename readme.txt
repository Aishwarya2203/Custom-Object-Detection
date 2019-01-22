Python 3.6 required
Tensorflow 1.0 required
OpenCV2 required
Protobuf required

*******************************************************************
Running the files
******************************************************************
Go to main/object-detection
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/ssd_mobilenet_v1_pets.config --trained_checkpoint_prefix training/model.ckpt-180 --output_directory aishwarya
Run the object_detection.py file
*****************************************************************
Custom Training
*****************************************************************
Use ImageLable for drawing bounding boxes
Convert Images to csv files using 

set TF_CPP_MIN_LOG_LEVEL=2
