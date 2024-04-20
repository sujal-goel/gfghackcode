document.getElementById('createBtn').addEventListener('click', function() {
    var comment = document.getElementById('comment').value;
    var tags = document.getElementById('tags').value.split(',').map(tag => tag.trim());

    var commentDiv = document.createElement('div');
    commentDiv.classList.add('comment');
    
    var commentText = document.createElement('p');
    commentText.textContent = "Comment: " + comment;
    commentDiv.appendChild(commentText);

    var tagsText = document.createElement('p');
    tagsText.textContent = "Tags: " + tags.join(', ');
    commentDiv.appendChild(tagsText);

    document.getElementById('commentArea').appendChild(commentDiv);

    document.getElementById('comment').value = '';
    document.getElementById('tags').value = '';
});
