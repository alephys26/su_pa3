def do(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    file.close()
    processed_lines = [line.strip().replace('.wav ','.wav:') for line in lines]
    processed_lines = [line.strip().replace('.mp3 ','.mp3:') for line in processed_lines]

    with open(file_name, 'w') as file:
        file.write('\n'.join(processed_lines))
    file.close()
    
# do('protocol/protocol_custom.txt')
do('/home/yash26/SU/PA3/protocol/protocol_test_for.txt')
do('/home/yash26/SU/PA3/protocol/protocol_train_for.txt')
do('/home/yash26/SU/PA3/protocol/protocol_val_for.txt')
# do('/home/yash26/SU/PA3/scores/eval_custom_DF.txt')
# do('/home/yash26/SU/PA3/scores/eval_custom_LA.txt')