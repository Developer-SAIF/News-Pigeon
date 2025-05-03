import Card from "react-bootstrap/Card";

function WithHeaderAndQuoteExample() {
  return (
    <>
      <Card className="text-center">
        <Card.Header></Card.Header>
        <Card.Body>
          <Card.Title>
            All the news are owned by their respected publishers.
          </Card.Title>
          <Card.Text>
            It may take upto 1 minute to load the news. Have patients or report
            inconsistency at{" "}
            <cite title="Source Title">Whatsapp: 01521774785 ~ Saif</cite>.
          </Card.Text>
        </Card.Body>
      </Card>
    </>
  );
}

export default WithHeaderAndQuoteExample;
