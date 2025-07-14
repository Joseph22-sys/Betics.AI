// Osler Score Line Chart
  new Chart(document.getElementById('oslerChart'), {
    type: 'line',
    data: {
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      datasets: [{
        label: 'Score',
        data: [70, 85, 80, 90, 1000, 87, 60],
        backgroundColor: 'rgba(16, 185, 129, 0.2)',
        borderColor: 'rgba(5, 150, 105, 1)',
        borderWidth: 2
      }]
    }
  });

  // Chatbot Messages Pie
  new Chart(document.getElementById('chatbotPie'), {
    type: 'doughnut',
    data: {
      labels: ['Responded', 'Pending'],
      datasets: [{
        data: [75, 25],
        backgroundColor: ['#10B981', '#FBBF24']
      }]
    }
  });

  // BP Multi-Line Chart
  new Chart(document.getElementById('bpChart'), {
    type: 'line',
    data: {
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      datasets: [
        {
          label: 'Systolic',
          data: [120, 118, 122, 121, 119, 124, 120],
          borderColor: '#4ADE80',
          fill: false
        },
        {
          label: 'Diastolic',
          data: [80, 78, 79, 77, 76, 81, 79],
          borderColor: '#60A5FA',
          fill: false
        }
      ]
    }
  });

    