from Day3_pipeline.data_loader import load_data


def test_load_data():
    data = load_data()
    assert data is not None
    assert hasattr(data, "data")
    assert hasattr(data, "target")
    assert len(data.data) > 0
    assert len(data.target) > 0
