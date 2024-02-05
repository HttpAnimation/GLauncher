import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.stage.Stage;

public class GLauncher extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Create a label with the text "Test"
        Label label = new Label("Test");

        // Create a scene with the label
        Scene scene = new Scene(label, 200, 100);

        // Set the scene to the primary stage
        primaryStage.setScene(scene);

        // Set the title of the window
        primaryStage.setTitle("Test Window");

        // Show the window
        primaryStage.show();
    }

    public static void main(String[] args) {
        // Launch the JavaFX application
        launch(args);
    }
}
