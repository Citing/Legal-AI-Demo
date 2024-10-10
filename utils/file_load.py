import streamlit as st
import os
import docx

class FileLoader():
    def __init__(self, fileName):
        self.fileName = fileName
        self.docName = os.path.splitext(fileName.name)[0]
        self.__type = os.path.splitext(fileName.name)[1].lower()
        self.__fileContent = self.__readContent(fileName)
        self.__chunks = []
        self.chunk_embeddings = {}

    def __readContent(self, fileName):
        if self.__type == ".txt":
            return fileName.read().decode("utf-8")
        elif self.__type == ".docx":
            return self.__read_docx(fileName)
    
    def __read_docx(self, fileName):
        doc = docx.Document(fileName)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    
    def __textSplitNaive(self, chunkSize):
        words = self.__fileContent.split()
        return [' '.join(words[i:i+chunkSize]) for i in range(0, len(words), chunkSize)]

    def textSplit(self, method="naive", chunkSize=100):
        if method == "naive":
            self.__chunks = self.__textSplitNaive(chunkSize)
        return self.__chunks
    


