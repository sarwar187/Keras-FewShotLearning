from keras_fsl.models.layers.support_layer import SupportLayer


class GramMatrix(SupportLayer):
    """
    Compute the gram matrix of the input batch using the given function. Note that this function can be learnt (if
    given a layer for instance).
    """

    def build_support_set(self, inputs):
        return inputs
