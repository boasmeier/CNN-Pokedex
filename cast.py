from PySide6 import QtGui, QtCore


class QPixmap2QByteArray(object):
    def __call__(self, q_image: QtGui.QImage) -> QtCore.QByteArray:
        """
            Args:
                q_image: QImage to be converted to byte stream.
                
            Returns:
                The byte array converted from q_image.
        """
        # Get an empty byte array
        byte_array = QtCore.QByteArray()
        # Bind the byte array to the output stream
        buffer = QtCore.QBuffer(byte_array)
        buffer.open(QtCore.QIODevice.WriteOnly)
        # Save the data in png format
        q_image.save(buffer, "png", quality=100)
        return byte_array
