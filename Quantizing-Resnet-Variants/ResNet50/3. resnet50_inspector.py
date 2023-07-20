import torch
from pytorch_nndct.apis import Inspector
from resnet50_model import ResNet50

target = "DPUCZDX8G_ISA1_B4096"
# Initialize inspector with target
inspector = Inspector(target)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the model to be inspected
model = ResNet50(image_channels=3, num_classes=3)
model.load_state_dict(torch.load("ResNet50.pth", map_location=torch.device('cpu')))

# Random input
dummy_input = torch.randn(1,3,224,224)

# Start to inspect
inspector.inspect(model, (dummy_input,), device=device, output_dir="inspect", image_format="png") 
