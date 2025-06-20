import React, { Component } from "react";
import NewsItem from "./NewsItem";
import Loading from "./Loading";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";


export class News extends Component {
  initialPage = 1;

  constructor() {
    super();
    this.state = {
      articles: [],
      loading: false,
      page: this.initialPage,
    };
  }

  fetchNews = (page = this.initialPage) => {
    this.setState({ loading: true });

    fetch(`${import.meta.env.VITE_API_BASE_URL}/api/update-news?page=${page}`)
      .then((res) => res.json())
      .then((data) => {
        this.setState({
          articles: data,
          loading: false,
          page,
        });
      })
      .catch((error) => {
        console.error("Error fetching news:", error);
        this.setState({ loading: false });
      });
  };

  componentDidMount() {
    this.fetchNews(this.initialPage);
  }

  handleNextClick = () => {
    const nextPage = this.state.page + 1;
    this.fetchNews(nextPage);
  };

  handlePrevClick = () => {
    const prevPage = this.state.page > this.initialPage ? this.state.page - 1 : this.initialPage;
    this.fetchNews(prevPage);
  };

  render() {
    return (
      <Container className="my-3">
        <h2>News Pigeon - Top headlines</h2>
        <Row className="row">
          {this.state.articles.map((element) => {
            return (
              <Col className="col-md-4" key={element.news_url}>
                <NewsItem
                  title={element.headline}
                  description={element.description}
                  imageUrl={element.image_url}
                  newsUrl={element.news_url}
                />
              </Col>
            );
          })}
        </Row>
        <Loading isLoading={this.state.loading} />
        <div className="my-3 container d-flex justify-content-between">
          <Button
            variant="success"
            onClick={this.handlePrevClick}
            disabled={this.state.page <= this.initialPage}
          >
            &lArr; Previous
          </Button>
          <div>
            <strong>Page: {this.state.page}</strong>
          </div>
          <Button variant="success" onClick={this.handleNextClick}>
            Next &rArr;
          </Button>
        </div>
      </Container>
    );
  }
}

export default News;
