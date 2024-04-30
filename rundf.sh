for ((i = 0; i <= 30; i++)); do
    echo "Current value of i: $i"

    CUDA_VISIBLE_DEVICES=0 python3 main_SSL_DF.py --is_eval --eval --model_path='models/Best_LA_model_for_DF.pth' --eval_output='eval_custom_DF.txt' --protocols_path="metadata_custom$i.txt" --database_path='data/Dataset_Speech_Assignment/Dataset_Speech_Assignment/Combined'
done
