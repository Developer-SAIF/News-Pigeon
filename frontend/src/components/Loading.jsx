import Alert from "react-bootstrap/Alert";
import Spinner from "react-bootstrap/Spinner";
import PropTypes from "prop-types";

function Loading({ isLoading }) {
  if (isLoading) {
    return (
      <Alert
        variant="success"
        style={{
          position: "fixed",
          top: "50%",
          left: "50%",
          transform: "translate(-50%, -50%)",
          zIndex: 2,
        }}
        className="p-4"
      >
        <Alert.Heading>
          <Spinner animation="grow"  className="me-3" />
          <strong>Loading</strong>
        </Alert.Heading>
      </Alert>
    );
  } else return null;
}

export default Loading;

Loading.propTypes = {
  loading: PropTypes.bool.isRequired,
};
