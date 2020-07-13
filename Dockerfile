FROM zainarbani/dockerub:one4u-alpine

RUN mkdir /NFSGang && chmod 777 /NFSGang
ENV PATH="/NFSGang/bin:$PATH"
WORKDIR /NFSGang

RUN git clone https://github.com/HafizZiq/NFS-Gang -b master /NFSGang

#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /NFSGang/

#
# Finalization
#
CMD ["python3","-m","userbot"]