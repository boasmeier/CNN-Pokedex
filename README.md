# CNN-Pokedex
A smallerVGGNet-Model (pyimagesearch.com) was trained to classify five diefferent pokemons (pikachu, bulbasaur, charmander, mewtwo, squirtle). You can either start the GUI or run the classify.py script in the CLI.

## Train
The python script train.py creates a trained model, a lb.pickle file and polts the train results.
> python train.py --dataset [path to dataset] --model [name of model to create] --labelbin [name of lb.pickel to create]

Example:
> python train.py --dataset dataset --model pokedex.model --labelbin lb.pickle

## Classify
The script classify.py classifies an example image and shows the image with the result.
> python classify.py --model [path to trained model] --labelbin [path to pickle file] --image [path to image]

Example:
> python classify.py --model pokedex.model --labelbin lb.pickle --image examples\pikachu.png

## GUI
The script index.py starts the GUI.
![gui] (gui.png)