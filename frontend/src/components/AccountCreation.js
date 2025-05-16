import { Card, Button, Container, Row, Col, Form, Dropdown } from 'react-bootstrap';
import { useState, useEffect } from 'react';
import axios from 'axios';

const AccountCreation = () => {
    const [selected, setSelected] = useState([]);
    const [tags,setTags] = useState([]);
    const [load,setLoad] = useState(false)
    const [formInfo,setFormInfo] = useState({
        firstName: "",
        lastName: "",

    })

    useEffect(() => {

        const setOption = (list) => {
            const formattedTags = list.map((item) => ({
                id: item.id,
                label: item.name,
            }))
            setTags(formattedTags)
            setLoad(true)
        }

        const getTags = async () => {
            const response = await axios.get("http://localhost:5000/tag/get_all_tags")
            setOption(response.data)
        }
        getTags()
    },[])

    const handleCheckboxChange = (id) => {
        setSelected((prev) =>
            prev.includes(id) ? prev.filter((item) => item !== id) : [...prev, id]
        );
    };

    const getSelectedLabels = () =>
        tags.filter(tag => selected.includes(tag.id)).map(tag => tag.label).join(', ');

    return (
        <Container className="mt-4">
            <Row>
                <Col md={{ span: 6, offset: 3 }}>
                    <Card>
                        <Card.Header>
                            <Card.Title className="mb-0">Please Complete Your Registration</Card.Title>
                        </Card.Header>
                        <Card.Body>
                            <Form>
                                <Form.Group>
                                    <Form.Label>Select Interests</Form.Label>
                                    <Dropdown>
                                        <Dropdown.Toggle variant="secondary" id="dropdown-basic">
                                            {selected.length ? getSelectedLabels() : 'Select Interests'}
                                        </Dropdown.Toggle>

                                        <Dropdown.Menu style={{ padding: '10px' }}>
                                            {load ? tags.map(({ id, label }) => (
                                                <Form.Check
                                                    key={id}
                                                    type="checkbox"
                                                    label={label}
                                                    checked={selected.includes(id)}
                                                    onChange={() => handleCheckboxChange(id)}
                                                    onClick={(e) => e.stopPropagation()} // prevent dropdown from closing
                                                />
                                            )): null}
                                        </Dropdown.Menu>
                                    </Dropdown>
                                </Form.Group>
                                <Button className="mt-3" variant="primary" type="submit">
                                    Register
                                </Button>
                            </Form>
                        </Card.Body>
                    </Card>
                </Col>
            </Row>
        </Container>
    );
};

export default AccountCreation;
