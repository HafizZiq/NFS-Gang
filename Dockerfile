FROM movecrew/one4ubot:alpine-latest

RUN mkdir /NFSGang && chmod 777 /NFSGang
ENV PATH="/NFSGang/bin:$PATH"
WORKDIR /NFSGang

RUN git clone https://github.com/HafizZiq/NFS-Gang -b master /NFSGang

#
# Make open port TCP
#
EXPOSE 80 443

#
# Finalization
#
CMD ["python3","-m","userbot"]
