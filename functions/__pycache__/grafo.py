�
    ��g.  �                   �&   � d dl Zd dlZd dlmZ d� Zy)�    Nc                  ��   � t        j                  d�      } t        j                  �       }| j	                  �       D ]"  \  }}|j                  |d   |d   |d   ��       �$ |S )Nz./functions/metro_santiago.csv�origen�destino�tiempo)�weight)�pd�read_csv�nx�Graph�iterrows�add_edge)�data�G�index�rows       �O/home/simuladordefarm3/Documentos/Universidad/grafos_trabajo/functions/grafo.py�grafo_metror      sY   � ��;�;�7�8�D� 	���
�A� �m�m�o�
��s�	�
�
�3�x�=�#�i�.��X��
�G� &� �H�    )�pandasr   �networkxr
   �matplotlib.pyplot�pyplot�pltr   � r   r   �<module>r      s   �� � � ��dr   