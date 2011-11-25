

frequencies = { "RF":4,
                "SF":36,
                "4K":624,
                "FH":3744,
                "FL":5108,
                "SR":10200,
                "3K":54912,
                "2P":123552,
                "1P":1098240,
                "HC":1302540,
                }

probabilities = { x:frequencies[x]/2598960.0 for x in frequencies}
