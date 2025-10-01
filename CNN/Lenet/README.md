# LENET


LeNet Diagram (Text Version)

            Input: 32x32
                ↓
    C1: Conv 5x5 → 6 maps → 28x28x6
                ↓
        S2: Avg Pool 2x2 → 14x14x6
                ↓
    C3: Conv 5x5 → 16 maps → 10x10x16
                ↓
        S4: Avg Pool 2x2 → 5x5x16
                ↓
    C5: Conv 5x5 → 120 maps → 1x1x120
                ↓
        F6: Fully Connected → 84 neurons
                ↓
        Output: 10 classes

                
