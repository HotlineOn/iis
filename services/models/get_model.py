import mlflow
import pickle as pkl

   
if __name__ == "__main__":
    # Работаем с MLflow локально
    TRACKING_SERVER_HOST = "127.0.0.1"
    TRACKING_SERVER_PORT = 5000

    registry_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"
    tracking_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"

    mlflow.set_tracking_uri(tracking_uri)   
    mlflow.set_registry_uri(registry_uri)   

    RUN_NAME = '862d49710c624401bb28470269c7c94b'
    print("trying to load from mlflow")
    loaded_model = mlflow.sklearn.load_model(f'runs:/{RUN_NAME}/models')
    print("model loaded")

    with open('model.pkl', 'wb+') as f:
        pkl.dump(loaded_model, f)

    print("model saved")
