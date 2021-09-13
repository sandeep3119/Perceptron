from utils.model import Perceptron
from utils.all_utils import prepare_data, save_model, save_plot
import pandas as pd

def main(data,eta,epochs,filename,imagefilename):
  
    df = pd.DataFrame(data)

    print(df)

    X, y = prepare_data(df)
    model = Perceptron(eta=eta, epochs=epochs)
    model.fit(X, y)

    _ = model.total_loss()

    save_model(model, filename=filename)
    save_plot(df, imagefilename, model=model)

if __name__ == '__main__': 
    OR = {
        "x1": [0, 0, 1, 1],
        "x2": [0, 1, 0, 1],
        "y": [0, 1, 1, 1],
    }
    
    ETA = 0.3  # 0 and 1
    EPOCHS = 10
    main(data=OR,eta=ETA,epochs=EPOCHS,filename='or.model',imagefilename='or.png')