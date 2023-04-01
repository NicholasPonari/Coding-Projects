import React from "react";
import { Container, Row, Col } from "reactstrap";
import Image from "next/image";

const Hero = () => {
  return (
    <section className="section position-relative">
      <Container>
        <Row className="align-items-center">
          <Col lg={6}>
            <div className="pr-lg-5">
              <p className="text-uppercase text-primary font-weight-medium f-14 mb-4">
                Discover the power of community
              </p>
              <h1 className="mb-4 font-weight-normal line-height-1_4">
                Welcome to
                <span className="text-primary font-weight-medium"> WeTF</span>,
                the world&apos;s first community-managed fund
              </h1>
              <p className="text-muted mb-4 pb-2">
                Everyone can&apos;t be an expert at everything. Join forces with
                thousands of others and unlock the benefits achievable only by
                working together.
              </p>
              <a href="#" className="btn btn-warning">
                Find Out How <span className="ml-2 right-icon">&#8594;</span>
              </a>
            </div>
          </Col>
          <Col lg={6}>
            <div className="mt-5 mt-lg-0">
              <Image src="/community.jpg" alt="logo" width="500" height="333" />
            </div>
          </Col>
        </Row>
      </Container>
    </section>
  );
};
export default Hero;
