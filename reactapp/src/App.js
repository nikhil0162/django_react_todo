import React, { useEffect, useState } from 'react'
import './App.css'
import PostLoading from './components/PostLoading'
import Posts from './components/Posts'
import Modal from './components/Modal';
import styled from 'styled-components';


const Container = styled.div`
  display:flex;
  justify-content:center;
  align-items:center;
  height:100vh;
`

const Button = styled.button`
  min-width: 100px;
  padding: 16px 32px;
  border-radius: 4px;
  background: #141414;
  color: #fff;
  font-size: 24px;
  cursor: pointer;
`


function App() {
  // const PostLoading = PostLoadingComponent(Posts);
  const [appState, setAppState] = useState({ loading: false, posts: null });
  const [showModal, setShowModal] = useState(false);


  useEffect(() => {
    setAppState({ loading: true });
    fetch('http://localhost:9000/api/')
      .then((data) => data.json())
      .then((posts) => {
        setAppState({ loading: false, posts: posts });
      });
  }, [setAppState])


  const openModal = () => {
    setShowModal(prevState => !prevState)
  };

  return (
    <div className="App">
      <h1>Latest Posts</h1>
      <Container>
        <Button onClick={openModal}>I'm a modal</Button>
        <Modal showModal={showModal} setShowModal={setShowModal} />
      </Container>

      {/* <PostLoading isLoading={appState.loading} posts={appState.posts} /> */}
    </div>
  );

}

export default App