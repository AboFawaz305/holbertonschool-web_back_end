export default class AppController {
  static getHomepage(_, res) {
    res.writeHead(200, {
      'Content-Type': 'text/plain',
    });
    res.end('Hello Holberton School!');
  }
}
