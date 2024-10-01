import streamlit as st
from utils.ai import textEmbedding
import os

class FileLoader():
    def __init__(self, fileName):
        self.docName = os.path.splitext(fileName.name)[0]
        self.__file_content = fileName.read().decode("utf-8")
        self.__chunks = []
        self.chunk_embeddings = {}
    
    def __textSplitNaive(self, chunkSize):
        words = self.__file_content.split()
        return [' '.join(words[i:i+chunkSize]) for i in range(0, len(words), chunkSize)]

    def textSplit(self, method="naive", chunkSize=100):
        if method == "naive":
            self.__chunks = self.__textSplitNaive(chunkSize)
        return self.__chunks

