#!/usr/bin/env bash
trap 'exit 2' 2
DIR=$(cd $(dirname $0); pwd)
CODE=${DIR}/src
CORPUS=${DIR}/corpus
SRC=input
TRG=target
BERT_MODEL=bert-base-multilingual-cased

#
# Split gec.txt file
# Tạo các file
# - gec.input.txt
# - gec.target.txt
# Sau đó tách ra thành tập train (70%) và tập test (30%)
# - train.input.txt
# - train.target.txt
# - test.input.txt
# - test.target.txt
# Tiếp theo, trong tập train lấy ra 20% làm tập validation
# - val.input.txt
# - val.target.txt
python ${CODE}/gec_data_split.py


#
# Train sub-word models
# Tạo các file:
# - train.spm.target.model
# - train.spm.target.vocab
# - train.spm.target.log
#
echo "Start train sub-word models"
### SentencePiece
sp_encode () {
    lang=$1
    size=$2
    spm_train --model_prefix=${CORPUS}/train.spm.${lang} \
	      --input=${CORPUS}/train.${lang}.txt \
	      --vocab_size=${size} \
	      --character_coverage=1.0 \
	      > ${CORPUS}/train.spm.${lang}.log 2>&1
}

if [[ ! -f ${CORPUS}/train.spm.${TRG}.log ]]; then
    # 22085 theo gợi ý spm_train() báo lỗi phải set vocab_size<= 22085 khi lần đầu set quá cao
    sp_encode ${TRG} 22085 &
    wait
fi
echo 'Done'

#
# Apply the sub-word models
# Tạo các file:
# - train.bpe.target  (sp_decode)
# - train.bpe.input   (bert_decode)
# - test.bpe.target
# - test.bpe.input
# - val.bpe.target
# - val.bpe.input
#
echo "Start apply the sub-word models"
### SentencePiece
sp_decode () {
    lang=$1
    testset=$2
    cat ${CORPUS}/${testset}.${lang}.txt \
	| spm_encode --model=${CORPUS}/train.spm.${lang}.model \
	> ${CORPUS}/${testset}.bpe.${lang}
}

### BERT tokenizer
bert_decode () {
    lang=$1
    testset=$2
    model=$3
    cat ${CORPUS}/${testset}.${lang}.txt \
	| python ${CODE}/bert_tokenize.py \
		  --model=${model} \
		  > ${CORPUS}/${testset}.bpe.${lang}
}

if [[ ! -f ${CORPUS}/train.bpe.${TRG} ]]; then
    for testset in train test val; do
        sp_decode   ${TRG} ${testset} &
        bert_decode ${SRC} ${testset} ${BERT_MODEL} &
        wait
    done
fi
echo 'Done'